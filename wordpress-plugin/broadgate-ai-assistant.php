<?php
/**
 * Plugin Name: Broadgate AI Assistant
 * Plugin URI: https://broadgate.ai
 * Description: Integrate Broadgate AI voice assistant into your WordPress site with a simple shortcode
 * Version: 1.0.0
 * Author: Broadgate
 * Author URI: https://broadgate.ai
 * License: GPL v2 or later
 * Text Domain: broadgate-ai
 */

// Prevent direct access
if (!defined('ABSPATH')) {
    exit;
}

// Define plugin constants
define('BROADGATE_AI_VERSION', '1.0.0');
define('BROADGATE_AI_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('BROADGATE_AI_PLUGIN_URL', plugin_dir_url(__FILE__));

// Include required files
require_once BROADGATE_AI_PLUGIN_DIR . 'includes/class-broadgate-api.php';
require_once BROADGATE_AI_PLUGIN_DIR . 'includes/class-broadgate-admin.php';

/**
 * Main Plugin Class
 */
class Broadgate_AI_Assistant {
    
    private static $instance = null;
    
    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }
    
    private function __construct() {
        // Initialize admin settings
        if (is_admin()) {
            new Broadgate_Admin();
        }
        
        // Register shortcode
        add_shortcode('broadgate_ai', array($this, 'render_shortcode'));
        
        // Enqueue frontend assets
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'));
        
        // AJAX handlers
        add_action('wp_ajax_broadgate_create_conversation', array($this, 'ajax_create_conversation'));
        add_action('wp_ajax_nopriv_broadgate_create_conversation', array($this, 'ajax_create_conversation'));
        add_action('wp_ajax_broadgate_end_conversation', array($this, 'ajax_end_conversation'));
        add_action('wp_ajax_nopriv_broadgate_end_conversation', array($this, 'ajax_end_conversation'));
    }
    
    /**
     * Enqueue frontend CSS and JavaScript
     */
    public function enqueue_assets() {
        wp_enqueue_style(
            'broadgate-ai-frontend',
            BROADGATE_AI_PLUGIN_URL . 'assets/css/broadgate-frontend.css',
            array(),
            BROADGATE_AI_VERSION
        );
        
        wp_enqueue_script(
            'broadgate-ai-frontend',
            BROADGATE_AI_PLUGIN_URL . 'assets/js/broadgate-frontend.js',
            array('jquery'),
            BROADGATE_AI_VERSION,
            true
        );
        
        // Pass AJAX URL and nonce to JavaScript
        wp_localize_script('broadgate-ai-frontend', 'broadgateAI', array(
            'ajaxUrl' => admin_url('admin-ajax.php'),
            'nonce' => wp_create_nonce('broadgate_ai_nonce')
        ));
    }
    
    /**
     * Render the shortcode
     */
    public function render_shortcode($atts) {
        $atts = shortcode_atts(array(
            'button_text' => get_option('broadgate_button_text', '🎙️ Talk to Broadgate AI'),
            'button_color' => get_option('broadgate_button_color', '#3B82F6'),
        ), $atts);
        
        ob_start();
        ?>
        <div class="broadgate-ai-container">
            <button 
                class="broadgate-ai-button" 
                data-broadgate-trigger
                style="background-color: <?php echo esc_attr($atts['button_color']); ?>;"
            >
                <?php echo esc_html($atts['button_text']); ?>
            </button>
            
            <div class="broadgate-ai-modal" style="display: none;">
                <div class="broadgate-ai-modal-content">
                    <button class="broadgate-ai-close" data-broadgate-close>&times;</button>
                    <div class="broadgate-ai-loading" style="display: none;">
                        <div class="broadgate-ai-spinner"></div>
                        <p>Starting conversation...</p>
                    </div>
                    <div class="broadgate-ai-iframe-container" style="display: none;">
                        <iframe 
                            class="broadgate-ai-iframe" 
                            allow="camera; microphone"
                            frameborder="0"
                        ></iframe>
                    </div>
                    <div class="broadgate-ai-error" style="display: none;">
                        <p class="error-message"></p>
                        <button class="broadgate-ai-retry">Try Again</button>
                    </div>
                </div>
            </div>
        </div>
        <?php
        return ob_get_clean();
    }
    
    /**
     * AJAX: Create conversation
     */
    public function ajax_create_conversation() {
        check_ajax_referer('broadgate_ai_nonce', 'nonce');
        
        $api = new Broadgate_API();
        $result = $api->create_conversation();
        
        if (is_wp_error($result)) {
            wp_send_json_error(array(
                'message' => $result->get_error_message()
            ));
        } else {
            wp_send_json_success($result);
        }
    }
    
    /**
     * AJAX: End conversation
     */
    public function ajax_end_conversation() {
        check_ajax_referer('broadgate_ai_nonce', 'nonce');
        
        $conversation_id = isset($_POST['conversation_id']) ? sanitize_text_field($_POST['conversation_id']) : '';
        
        if (empty($conversation_id)) {
            wp_send_json_error(array('message' => 'Conversation ID required'));
        }
        
        $api = new Broadgate_API();
        $result = $api->end_conversation($conversation_id);
        
        if (is_wp_error($result)) {
            wp_send_json_error(array(
                'message' => $result->get_error_message()
            ));
        } else {
            wp_send_json_success($result);
        }
    }
}

// Initialize the plugin
function broadgate_ai_init() {
    return Broadgate_AI_Assistant::get_instance();
}
add_action('plugins_loaded', 'broadgate_ai_init');
