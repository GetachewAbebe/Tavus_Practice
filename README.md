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