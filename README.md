# Broadgate

**Intelligent Voice Automation Platform** - Transform your customer interactions with AI-powered voice conversations.

## 🚀 Features

- 🎙️ **AI Voice Conversations** - Natural, context-aware voice interactions
- 📊 **Real-time Analytics** - Track performance and conversation metrics
- 🎨 **Custom Personas** - Create branded AI personalities
- 📝 **Knowledge Base Integration** - Connect your documentation
- 🔔 **Webhook Notifications** - Real-time alerts and integrations
- 💾 **Lead Capture** - Automatic extraction of names and emails
- 📈 **Export Capabilities** - Download conversation data as CSV

## 📋 Prerequisites

- Python 3.8 or higher
- Tavus API account ([sign up here](https://tavus.io))
- Modern web browser
- Microphone for voice conversations

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Tavus_Practice
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Tavus API key and other settings.

4. **Run setup script**
   ```bash
   python setup.py
   ```
   
   This will create your persona and provide a `BROADGATE_PERSONA_ID`. Add this to your `.env` file.

5. **Start the application**
   ```bash
   streamlit run app.py
   ```

## ☁️ Deploying to Streamlit Cloud

To deploy to Streamlit Cloud, you need to configure secrets instead of using a `.env` file:

1. Push your code to GitHub
2. Create a new app on [Streamlit Cloud](https://share.streamlit.io)
3. Set **Main file path** to: `app.py`
4. In your app's **Settings > Secrets**, add:

```toml
# Tavus API Key
API_KEY = "your_tavus_api_key_here"

# Broadgate Persona ID
BROADGATE_PERSONA_ID = "your_persona_id_here"

# Replica ID
REPLICA_ID = "your_replica_id_here"

# Voice Configuration
TTS_ENGINE = "elevenlabs"
BRITISH_VOICE_ID = "your_voice_id_here"

# Webhook URL (Optional)
WEBHOOK_URL = "https://your-webhook-endpoint.com/webhook"
```

5. Save and your app will automatically reboot

**📖 See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.**

## 📁 Project Structure

```
Tavus_Practice/
├── components/          # UI components
│   ├── __init__.py
│   ├── styling.py      # CSS and theming
│   ├── sidebar.py      # Sidebar component
│   └── modals.py       # Modal dialogs
├── utils/              # Utility functions
│   ├── __init__.py
│   ├── api.py         # Tavus API client
│   ├── database.py    # SQLite operations
│   ├── webhook.py     # Webhook handling
│   └── extraction.py  # Data extraction
├── pages/              # Streamlit pages
│   ├── 1_📊_Analytics.py
│   ├── 2_⚡_Features.py
│   ├── 3_❓_FAQ.py
│   └── 4_📧_Contact.py
├── assets/             # Media files
│   └── demo.gif
├── Konwledge_Base/     # Knowledge base documents
│   └── Broadgate.pdf
├── config.py           # Configuration
├── app.py              # Main entry point
├── setup.py            # Setup script
├── requirements.txt
├── .env.example        # Environment template
├── DEPLOYMENT.md       # Deployment guide
└── README.md
```

## 🎯 Usage

### Starting a Conversation

1. Navigate to the **Home** page
2. Click **"Start Conversation"**
3. Allow microphone access when prompted
4. Start talking naturally with the AI

### Viewing Analytics

1. Navigate to the **Analytics** page
2. View conversation metrics and captured leads
3. Export data to CSV if needed

### Customizing Your Persona

Edit `setup.py` to customize:
- **PERSONA_NAME**: Your persona's name
- **PERSONA_SYSTEM_PROMPT**: Behavior and personality
- **KNOWLEDGE_BASE_URL**: Your knowledge base document

Then run `python setup.py` to update.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `API_KEY` | Tavus API key | Yes | - |
| `BROADGATE_PERSONA_ID` | Generated persona ID | Yes | - |
| `REPLICA_ID` | Default replica ID | No | `your_replica_id` |
| `TTS_ENGINE` | Text-to-Speech Engine | No | `elevenlabs` |
| `BRITISH_VOICE_ID` | Voice ID for ElevenLabs | No | `your_voice_id` |
| `WEBHOOK_URL` | Webhook endpoint URL | No | - |

**Local Development:** Use `.env` file  
**Streamlit Cloud:** Use Secrets (TOML format)

The app automatically detects which environment it's running in.

### Database

Conversations and leads are stored in `broadgate_leads.db` (SQLite).

## 🔗 Webhooks

Configure webhooks to receive real-time notifications:

**Payload Format:**
```json
{
  "conversation_id": "conv_123",
  "name": "John Doe",
  "email": "john@example.com",
  "transcript": "Full conversation text...",
  "timestamp": "2024-12-01T12:00:00Z"
}
```

Set `WEBHOOK_URL` in your `.env` file or Streamlit Cloud secrets to enable.

## 📊 Analytics

The Analytics dashboard provides:
- Total conversation count
- Lead capture metrics
- Conversion rates
- Recent conversation history
- CSV export functionality

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: Check the FAQ page in the app
- **Issues**: Open an issue on GitHub
- **Email**: support@broadgate.ai

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Powered by [Tavus API](https://tavus.io)
- AI voice technology by Tavus

---

**Broadgate** - Intelligent Voice Automation Platform © 2024