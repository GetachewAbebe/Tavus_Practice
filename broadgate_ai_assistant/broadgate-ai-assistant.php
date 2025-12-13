<?php
/**
 * Plugin Name: Broadgate AI Assistant
 * Plugin URI: https://broadgate.ai
 * Description: Adds a floating Broadgate AI assistant widget to the bottom-right corner of your WordPress site.
 * Version: 4.9.3
 * Author: Broadgate
 * License: GPL v2 or later
 * Text Domain: broadgate-ai
 */

if (!defined('ABSPATH')) exit;

define('BROADGATE_AI_VERSION', '4.9.3');
define('BROADGATE_AI_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('BROADGATE_AI_PLUGIN_URL', plugin_dir_url(__FILE__));

$api_file   = BROADGATE_AI_PLUGIN_DIR . 'includes/class-broadgate-api.php';
$admin_file = BROADGATE_AI_PLUGIN_DIR . 'includes/class-broadgate-admin.php';

if (!file_exists($api_file)) {
    add_action('admin_notices', function () use ($api_file) {
        echo '<div class="notice notice-error"><p><strong>Broadgate AI Assistant:</strong> Missing file: '
            . esc_html($api_file) . '</p></div>';
    });
    return;
}
require_once $api_file;

if (file_exists($admin_file)) {
    require_once $admin_file;
}

class Broadgate_AI_Assistant {
    private static $rendered = false;

    public function __construct() {
        if (is_admin() && class_exists('Broadgate_Admin')) {
            new Broadgate_Admin();
        }

        add_action('wp_enqueue_scripts', [$this, 'enqueue_assets']);
        add_action('wp_footer', [$this, 'render_floating_widget'], 9999);

        add_shortcode('broadgate_ai_assistant', [$this, 'render_shortcode']);
        add_shortcode('broadgate_ai', [$this, 'render_shortcode']);

        add_action('wp_ajax_broadgate_create_conversation', [$this, 'ajax_create_conversation']);
        add_action('wp_ajax_nopriv_broadgate_create_conversation', [$this, 'ajax_create_conversation']);

        // ✅ NEW: fetch Tavus avatar preview URL on page load
        add_action('wp_ajax_broadgate_get_avatar', [$this, 'ajax_get_avatar']);
        add_action('wp_ajax_nopriv_broadgate_get_avatar', [$this, 'ajax_get_avatar']);
    }

    public function enqueue_assets() {
        if (is_admin()) return;

        wp_enqueue_style(
            'broadgate-ai-css',
            BROADGATE_AI_PLUGIN_URL . 'assets/css/broadgate-frontend.css',
            [],
            BROADGATE_AI_VERSION
        );

        wp_enqueue_script(
            'daily-js',
            'https://unpkg.com/@daily-co/daily-js',
            [],
            null,
            true
        );

        wp_enqueue_script(
            'broadgate-ai-js',
            BROADGATE_AI_PLUGIN_URL . 'assets/js/broadgate-frontend.js',
            ['jquery', 'daily-js'],
            BROADGATE_AI_VERSION,
            true
        );

        $payload = [
            'ajaxurl' => admin_url('admin-ajax.php'),
            'nonce'   => wp_create_nonce('broadgate_nonce'),
        ];
        wp_localize_script('broadgate-ai-js', 'broadgateAjax', $payload);
        wp_localize_script('broadgate-ai-js', 'broadgateAI',   $payload);
    }

    public function render_floating_widget() {
        if (is_admin()) return;
        if (self::$rendered) return;

        echo $this->render_widget_markup([
            // fallback local video ONLY if Tavus avatar URL cannot be fetched
            'fallback_avatar' => BROADGATE_AI_PLUGIN_URL . '7202eb45.mp4',
            'button_text'     => 'TALK NOW',
            'button_color'    => '#3B82F6',
        ]);

        self::$rendered = true;
    }

    public function render_shortcode($atts) {
        self::$rendered = true;

        $atts = shortcode_atts([
            'fallback_avatar' => BROADGATE_AI_PLUGIN_URL . '7202eb45.mp4',
            'button_text'     => 'TALK NOW',
            'button_color'    => '#3B82F6',
        ], $atts);

        return $this->render_widget_markup($atts);
    }

    private function render_widget_markup($atts) {
        $fallback_avatar = esc_url($atts['fallback_avatar']);
        $button_text     = esc_html($atts['button_text']);
        $btn_color       = esc_attr($atts['button_color']);

        ob_start(); ?>
        <div id="broadgate-ai-container">
            <div id="broadgate-ai-card">

                <div id="broadgate-ai-header">
                    <button class="broadgate-ai-close" id="broadgate-ai-close" aria-label="Close">✕</button>
                </div>

                <!-- ✅ Idle avatar (src will be replaced by Tavus URL on load) -->
                <div class="broadgate-ai-avatar-wrapper" id="broadgate-ai-idle">
                    <video
                        id="broadgate-ai-idle-video"
                        class="broadgate-ai-avatar-video"
                        autoplay
                        muted
                        loop
                        playsinline
                        preload="auto"
                        data-fallback-src="<?php echo $fallback_avatar; ?>"
                    >
                        <source src="<?php echo $fallback_avatar; ?>" type="video/mp4">
                    </video>
                </div>

                <!-- Live AI assistant video during call -->
                <div id="broadgate-ai-remote-wrap" style="display:none;">
                    <video id="broadgate-ai-remote-video" autoplay playsinline></video>
                </div>

                <!-- Loading animation -->
                <div id="broadgate-ai-loading" style="display:none;">
                    <div class="broadgate-ai-loading-card" aria-label="Loading">
                        <div class="broadgate-ai-spinner"></div>
                        <div class="broadgate-ai-dots" aria-hidden="true">
                            <span></span><span></span><span></span>
                        </div>
                    </div>
                </div>

                <div id="broadgate-ai-error" style="display:none;"></div>

                <button
                    id="broadgate-ai-talk-now"
                    type="button"
                    style="background: <?php echo $btn_color; ?>; color:#fff;"
                ><?php echo $button_text; ?></button>

                <div id="broadgate-ai-controls" style="display:none;">
                    <button id="broadgate-ai-mute" type="button">Mute</button>
                    <button id="broadgate-ai-hangup" type="button">End</button>
                </div>

            </div>
        </div>
        <?php
        return ob_get_clean();
    }

    public function ajax_create_conversation() {
        check_ajax_referer('broadgate_nonce', 'nonce');

        $api = new Broadgate_API();
        $result = $api->create_conversation();

        if (is_wp_error($result)) {
            wp_send_json_error([
                'message' => $result->get_error_message(),
                'debug'   => $result->get_error_data(),
            ]);
        }

        wp_send_json_success($result);
    }

    // ✅ NEW: fetch Tavus avatar/preview video URL for idle looping
    public function ajax_get_avatar() {
        check_ajax_referer('broadgate_nonce', 'nonce');

        $api = new Broadgate_API();
        $result = $api->get_idle_avatar_video_url();

        if (is_wp_error($result)) {
            wp_send_json_error([
                'message' => $result->get_error_message(),
                'debug'   => $result->get_error_data(),
            ]);
        }

        wp_send_json_success($result);
    }
}

new Broadgate_AI_Assistant();
