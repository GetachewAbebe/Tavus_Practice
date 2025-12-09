<?php
/**
 * Broadgate API Integration Class
 * Handles communication with Tavus API
 */

class Broadgate_API {
    
    private $api_key;
    private $persona_id;
    private $replica_id;
    private $custom_greeting;
    private $api_base_url = 'https://tavusapi.com/v2';
    
    public function __construct() {
        $this->api_key = get_option('broadgate_api_key', '');
        $this->persona_id = get_option('broadgate_persona_id', '');
        $this->replica_id = get_option('broadgate_replica_id', '');
        $this->custom_greeting = get_option('broadgate_custom_greeting', 'Hello! I\'m Gigi from Broadgate. What can I help you with?');
    }
    
    /**
     * Create a new conversation
     */
    public function create_conversation() {
        if (empty($this->api_key) || empty($this->persona_id)) {
            return new WP_Error('missing_config', 'API Key and Persona ID are required. Please configure in plugin settings.');
        }
        
        $payload = array(
            'persona_id' => $this->persona_id,
            'conversational_context' => 'Start the conversation by greeting the user and introducing yourself.',
            'custom_greeting' => $this->custom_greeting
        );
        
        if (!empty($this->replica_id)) {
            $payload['replica_id'] = $this->replica_id;
        }
        
        $response = wp_remote_post($this->api_base_url . '/conversations', array(
            'headers' => array(
                'x-api-key' => $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'body' => json_encode($payload),
            'timeout' => 30
        ));
        
        if (is_wp_error($response)) {
            return $response;
        }
        
        $status_code = wp_remote_retrieve_response_code($response);
        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        
        if ($status_code !== 200) {
            $error_message = isset($data['message']) ? $data['message'] : 'Failed to create conversation';
            return new WP_Error('api_error', $error_message);
        }
        
        return array(
            'conversation_url' => isset($data['conversation_url']) ? $data['conversation_url'] : '',
            'conversation_id' => isset($data['conversation_id']) ? $data['conversation_id'] : ''
        );
    }
    
    /**
     * End a conversation
     */
    public function end_conversation($conversation_id) {
        if (empty($this->api_key)) {
            return new WP_Error('missing_config', 'API Key is required.');
        }
        
        if (empty($conversation_id)) {
            return new WP_Error('missing_id', 'Conversation ID is required.');
        }
        
        $response = wp_remote_post($this->api_base_url . '/conversations/' . $conversation_id . '/end', array(
            'headers' => array(
                'x-api-key' => $this->api_key,
                'Content-Type' => 'application/json'
            ),
            'timeout' => 30
        ));
        
        if (is_wp_error($response)) {
            return $response;
        }
        
        return array('status' => 'success', 'message' => 'Conversation ended');
    }
}
