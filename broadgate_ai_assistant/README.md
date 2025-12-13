# Broadgate AI Assistant - WordPress Plugin

A WordPress plugin that integrates the Broadgate AI voice assistant into your website using a simple shortcode.

## Features

- 🎙️ **Voice AI Integration** - Embed Broadgate AI assistant anywhere on your site
- ⚙️ **Easy Configuration** - Simple admin settings page
- 🎨 **Customizable** - Customize button text, colors, and greeting message
- 📱 **Responsive** - Works perfectly on desktop and mobile
- 🔒 **Secure** - Uses WordPress nonces and sanitization
- ⚡ **On-Demand** - Conversations start only when users click (cost-effective)

## Installation

### Method 1: Upload via WordPress Admin

1. Download the `broadgate-ai-assistant` folder
2. Zip the entire folder
3. Go to WordPress Admin → Plugins → Add New → Upload Plugin
4. Upload the zip file
5. Click "Install Now" and then "Activate"

### Method 2: Manual Installation

1. Download the `broadgate-ai-assistant` folder
2. Upload it to `/wp-content/plugins/` directory via FTP
3. Go to WordPress Admin → Plugins
4. Find "Broadgate AI Assistant" and click "Activate"

## Configuration

1. Go to **WordPress Admin → Broadgate AI**
2. Enter your configuration:
   - **Tavus API Key**: Your API key from Tavus
   - **Persona ID**: Your Broadgate persona ID (e.g., `p40adc27fe3a`)
   - **Replica ID**: (Optional) Your replica ID
   - **Custom Greeting**: The first message the AI will speak
   - **Button Text**: Text displayed on the button
   - **Button Color**: Button background color

3. Click "Save Changes"

## Usage

### Basic Shortcode

Add this shortcode to any page or post:

```
[broadgate_ai]
```

### Customized Shortcode

Override default settings with shortcode attributes:

```
[broadgate_ai button_text="Chat with Gigi" button_color="#FF5733"]
```

### Available Shortcode Attributes

- `button_text` - Custom button text
- `button_color` - Custom button color (hex code)

## Getting Your API Credentials

1. **API Key**:
   - Sign up at [Tavus API](https://tavusapi.com)
   - Go to your dashboard
   - Copy your API key

2. **Persona ID**:
   - You should already have this from your Streamlit app
   - It's in your `.env` file as `BROADGATE_PERSONA_ID`
   - Example: `p40adc27fe3a`

3. **Replica ID** (Optional):
   - Also in your `.env` file as `REPLICA_ID`
   - Example: `rc2146c13e81`

## How It Works

1. User clicks the "Talk to Broadgate AI" button
2. Plugin makes an AJAX call to create a new conversation via Tavus API
3. Conversation iframe loads in a modal
4. User can talk to the AI assistant
5. When modal closes, conversation ends automatically

## File Structure

```
broadgate-ai-assistant/
├── broadgate-ai-assistant.php    # Main plugin file
├── includes/
│   ├── class-broadgate-api.php   # API integration
│   └── class-broadgate-admin.php # Admin settings
├── assets/
│   ├── js/
│   │   └── broadgate-frontend.js # Frontend JavaScript
│   └── css/
│       └── broadgate-frontend.css # Frontend styles
└── README.md                      # This file
```

## Requirements

- WordPress 5.0 or higher
- PHP 7.2 or higher
- Tavus API account
- Broadgate persona configured

## Support

For issues or questions:
- Check your API credentials in plugin settings
- Ensure your Tavus account is active
- Check browser console for JavaScript errors
- Verify your persona ID is correct

## Version

**1.0.0** - Initial release

## License

GPL v2 or later

---

**Made with ❤️ for Broadgate**
