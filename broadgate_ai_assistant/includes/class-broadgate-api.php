<?php
if (!defined('ABSPATH')) exit;

class Broadgate_API {

    private $api_key;
    private $persona_id;
    private $replica_id;
    private $custom_greeting;

    // Tavus base
    private $api_base_url = 'https://tavusapi.com/v2';

    public function __construct() {
        $this->api_key         = get_option('broadgate_api_key');
        $this->persona_id      = get_option('broadgate_persona_id');
        $this->replica_id      = get_option('broadgate_replica_id');
        $this->custom_greeting = get_option('broadgate_custom_greeting', 'Hello! How can I assist you today?');
    }

    private function bg_log($label, $data = null) {
        $msg = '[BroadgateAI] ' . $label;
        if ($data !== null) {
            $msg .= ' ' . (is_array($data) || is_object($data) ? wp_json_encode($data) : (string)$data);
        }
        error_log($msg);
    }

    /**
     * ✅ Fetch a Tavus-hosted preview/idle avatar video URL.
     * - Caches for 6 hours to avoid hitting Tavus on every page load.
     * - Requires broadgate_replica_id in plugin settings.
     */
    public function get_idle_avatar_video_url() {
        $cache_key = 'broadgate_idle_avatar_url';
        $cached = get_transient($cache_key);
        if (!empty($cached)) {
            return ['avatar_url' => $cached, 'cached' => true];
        }

        if (empty($this->api_key)) {
            return new WP_Error('missing_config', 'API Key is required to fetch Tavus avatar.');
        }

        if (empty($this->replica_id)) {
            // We can’t guess which avatar to fetch without replica_id
            return new WP_Error('missing_config', 'Replica ID is required to fetch Tavus avatar preview video.');
        }

        // Common Tavus pattern: replicas/{replica_id}
        $url = $this->api_base_url . '/replicas/' . rawurlencode($this->replica_id);

        $this->bg_log('Fetching replica (idle avatar) -> GET ' . $url);

        $resp = wp_remote_get($url, [
            'headers' => [
                'x-api-key'    => $this->api_key,
                'Content-Type' => 'application/json',
            ],
            'timeout' => 45,
        ]);

        if (is_wp_error($resp)) {
            return $resp;
        }

        $status = wp_remote_retrieve_response_code($resp);
        $body   = wp_remote_retrieve_body($resp);

        $this->bg_log('Replica fetch status_code:', $status);
        $this->bg_log('Replica raw body:', $body);

        $data = json_decode($body, true);

        if ($status < 200 || $status >= 300 || !is_array($data)) {
            return new WP_Error('api_error', 'Failed to fetch replica avatar from Tavus.', [
                'status_code' => $status,
                'raw_body'    => $body,
                'raw_json'    => $data,
                'request_url' => $url,
            ]);
        }

        // Try common fields first
        $candidate =
            $data['preview_video_url']
            ?? ($data['data']['preview_video_url'] ?? null)
            ?? $data['idle_video_url']
            ?? ($data['data']['idle_video_url'] ?? null)
            ?? $data['video_url']
            ?? ($data['data']['video_url'] ?? null)
            ?? $data['avatar_video_url']
            ?? ($data['data']['avatar_video_url'] ?? null)
            ?? null;

        // Last resort: find first mp4 URL anywhere in the payload
        if (empty($candidate)) {
            $candidate = $this->find_first_mp4_url($data);
        }

        if (empty($candidate)) {
            return new WP_Error('api_error', 'Replica fetched but no preview mp4 URL was found. Check Tavus response fields in debug log.', [
                'raw_json' => $data
            ]);
        }

        // Cache for 6 hours
        set_transient($cache_key, (string)$candidate, 6 * HOUR_IN_SECONDS);

        return [
            'avatar_url' => (string)$candidate,
            'cached'     => false
        ];
    }

    private function find_first_mp4_url($value) {
        if (is_string($value)) {
            $v = $value;
            if ((stripos($v, 'http://') === 0 || stripos($v, 'https://') === 0) && preg_match('/\.mp4(\?|$)/i', $v)) {
                return $v;
            }
            return null;
        }
        if (!is_array($value)) return null;

        foreach ($value as $v) {
            $found = $this->find_first_mp4_url($v);
            if (!empty($found)) return $found;
        }
        return null;
    }

    public function create_conversation() {
        if (empty($this->api_key) || empty($this->persona_id)) {
            return new WP_Error(
                'missing_config',
                'API Key and Persona ID are required. Please configure in plugin settings.',
                ['missing' => ['api_key' => empty($this->api_key), 'persona_id' => empty($this->persona_id)]]
            );
        }

        $payload = [
            'persona_id'             => $this->persona_id,
            'conversational_context' => 'Start the conversation by greeting the user and introducing yourself.',
            'custom_greeting'        => $this->custom_greeting,
        ];

        if (!empty($this->replica_id)) {
            $payload['replica_id'] = $this->replica_id;
        }

        $url = $this->api_base_url . '/conversations';

        $this->bg_log('Creating conversation -> POST ' . $url);
        $this->bg_log('Payload:', $payload);

        $response = wp_remote_post($url, [
            'headers' => [
                'x-api-key'    => $this->api_key,
                'Content-Type' => 'application/json',
            ],
            'body'    => wp_json_encode($payload),
            'timeout' => 45,
        ]);

        if (is_wp_error($response)) {
            $this->bg_log('wp_remote_post error:', $response->get_error_message());
            return $response;
        }

        $status_code = wp_remote_retrieve_response_code($response);
        $body        = wp_remote_retrieve_body($response);

        $this->bg_log('Tavus status_code:', $status_code);
        $this->bg_log('Tavus raw body:', $body);

        $data = json_decode($body, true);

        if ($status_code < 200 || $status_code >= 300) {
            $msg = 'Failed to create conversation (HTTP ' . $status_code . ')';
            if (is_array($data) && !empty($data['message'])) $msg = $data['message'];

            return new WP_Error('api_error', $msg, [
                'status_code' => $status_code,
                'raw_body'    => $body,
                'raw_json'    => $data,
                'request_url' => $url,
                'request'     => $payload,
            ]);
        }

        if (!is_array($data)) {
            return new WP_Error('api_error', 'Invalid API response (not JSON).', [
                'status_code' => $status_code,
                'raw_body'    => $body,
                'request_url' => $url,
                'request'     => $payload,
            ]);
        }

        $conversation_url =
            $data['conversation_url']
            ?? ($data['data']['conversation_url'] ?? null)
            ?? $data['url']
            ?? ($data['data']['url'] ?? null)
            ?? null;

        $conversation_id =
            $data['conversation_id']
            ?? ($data['data']['conversation_id'] ?? null)
            ?? ($data['id'] ?? null)
            ?? null;

        if (empty($conversation_url)) {
            return new WP_Error('api_error', 'Conversation created but no conversation URL returned.', [
                'raw_json' => $data
            ]);
        }

        return [
            'conversation_url' => (string)$conversation_url,
            'conversation_id'  => $conversation_id ? (string)$conversation_id : '',
            'raw'              => $data,
        ];
    }
}
