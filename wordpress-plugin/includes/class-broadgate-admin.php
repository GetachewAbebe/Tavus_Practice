<?php
/**
 * Broadgate Admin Settings Class
 * Handles plugin settings page in WordPress admin
 */

class Broadgate_Admin {
    
    public function __construct() {
        add_action('admin_menu', array($this, 'add_admin_menu'));
        add_action('admin_init', array($this, 'register_settings'));
    }
    
    /**
     * Add admin menu page
     */
    public function add_admin_menu() {
        add_menu_page(
            'Broadgate AI Settings',
            'Broadgate AI',
            'manage_options',
            'broadgate-ai',
            array($this, 'render_settings_page'),
            'dashicons-format-chat',
            30
        );
    }
    
    /**
     * Register plugin settings
     */
    public function register_settings() {
        // API Settings Section
        add_settings_section(
            'broadgate_api_section',
            'API Configuration',
            array($this, 'render_api_section'),
            'broadgate-ai'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_api_key');
        add_settings_field(
            'broadgate_api_key',
            'Tavus API Key',
            array($this, 'render_api_key_field'),
            'broadgate-ai',
            'broadgate_api_section'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_persona_id');
        add_settings_field(
            'broadgate_persona_id',
            'Persona ID',
            array($this, 'render_persona_id_field'),
            'broadgate-ai',
            'broadgate_api_section'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_replica_id');
        add_settings_field(
            'broadgate_replica_id',
            'Replica ID (Optional)',
            array($this, 'render_replica_id_field'),
            'broadgate-ai',
            'broadgate_api_section'
        );
        
        // Customization Section
        add_settings_section(
            'broadgate_customization_section',
            'Customization',
            array($this, 'render_customization_section'),
            'broadgate-ai'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_custom_greeting');
        add_settings_field(
            'broadgate_custom_greeting',
            'Custom Greeting',
            array($this, 'render_greeting_field'),
            'broadgate-ai',
            'broadgate_customization_section'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_button_text');
        add_settings_field(
            'broadgate_button_text',
            'Button Text',
            array($this, 'render_button_text_field'),
            'broadgate-ai',
            'broadgate_customization_section'
        );
        
        register_setting('broadgate_ai_settings', 'broadgate_button_color');
        add_settings_field(
            'broadgate_button_color',
            'Button Color',
            array($this, 'render_button_color_field'),
            'broadgate-ai',
            'broadgate_customization_section'
        );
    }
    
    /**
     * Render settings page
     */
    public function render_settings_page() {
        ?>
        <div class="wrap">
            <h1>🎙️ Broadgate AI Assistant Settings</h1>
            
            <div class="notice notice-info">
                <p><strong>How to use:</strong> Add the shortcode <code>[broadgate_ai]</code> to any page or post to display the AI assistant.</p>
            </div>
            
            <form method="post" action="options.php">
                <?php
                settings_fields('broadgate_ai_settings');
                do_settings_sections('broadgate-ai');
                submit_button();
                ?>
            </form>
            
            <hr>
            
            <h2>📖 Documentation</h2>
            <h3>Shortcode Usage</h3>
            <p>Basic usage:</p>
            <pre><code>[broadgate_ai]</code></pre>
            
            <p>With custom button text:</p>
            <pre><code>[broadgate_ai button_text="Chat with Gigi"]</code></pre>
            
            <p>With custom button color:</p>
            <pre><code>[broadgate_ai button_color="#FF5733"]</code></pre>
            
            <h3>Getting Your API Credentials</h3>
            <ol>
                <li>Sign up at <a href="https://tavusapi.com" target="_blank">Tavus API</a></li>
                <li>Get your API Key from the dashboard</li>
                <li>Create a persona and copy the Persona ID</li>
                <li>Optionally, create a replica and copy the Replica ID</li>
            </ol>
        </div>
        <?php
    }
    
    // Section callbacks
    public function render_api_section() {
        echo '<p>Enter your Tavus API credentials below.</p>';
    }
    
    public function render_customization_section() {
        echo '<p>Customize the appearance and behavior of your AI assistant.</p>';
    }
    
    // Field callbacks
    public function render_api_key_field() {
        $value = get_option('broadgate_api_key', '');
        echo '<input type="password" name="broadgate_api_key" value="' . esc_attr($value) . '" class="regular-text" required>';
        echo '<p class="description">Your Tavus API key</p>';
    }
    
    public function render_persona_id_field() {
        $value = get_option('broadgate_persona_id', '');
        echo '<input type="text" name="broadgate_persona_id" value="' . esc_attr($value) . '" class="regular-text" required>';
        echo '<p class="description">Your Broadgate persona ID (e.g., p40adc27fe3a)</p>';
    }
    
    public function render_replica_id_field() {
        $value = get_option('broadgate_replica_id', '');
        echo '<input type="text" name="broadgate_replica_id" value="' . esc_attr($value) . '" class="regular-text">';
        echo '<p class="description">Optional: Your replica ID for the AI avatar</p>';
    }
    
    public function render_greeting_field() {
        $value = get_option('broadgate_custom_greeting', 'Hello! I\'m Gigi from Broadgate. What can I help you with?');
        echo '<textarea name="broadgate_custom_greeting" rows="3" class="large-text">' . esc_textarea($value) . '</textarea>';
        echo '<p class="description">The first message the AI will speak</p>';
    }
    
    public function render_button_text_field() {
        $value = get_option('broadgate_button_text', '🎙️ Talk to Broadgate AI');
        echo '<input type="text" name="broadgate_button_text" value="' . esc_attr($value) . '" class="regular-text">';
        echo '<p class="description">Text displayed on the conversation button</p>';
    }
    
    public function render_button_color_field() {
        $value = get_option('broadgate_button_color', '#3B82F6');
        echo '<input type="color" name="broadgate_button_color" value="' . esc_attr($value) . '">';
        echo '<p class="description">Button background color</p>';
    }
}
