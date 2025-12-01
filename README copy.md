# VoiceFlow AI

**Intelligent Voice Automation Platform**

VoiceFlow AI is an enterprise-grade voice automation platform powered by advanced AI. Built on the Tavus API, it enables businesses to deploy human-like voice agents for customer support, sales, and operations.

## 🚀 Features

- **🧠 Contextual Intelligence** - Maintains conversation context and understands intent
- **⚡ Real-time Interaction** - Sub-second latency for natural conversation flow
- **🔒 Enterprise Security** - SOC2 compliant with end-to-end encryption
- **📊 Analytics Dashboard** - Real-time performance monitoring and insights
- **🔌 Easy Integration** - Connect with 50+ tools including Salesforce, HubSpot, Zendesk
- **🌐 Multi-Language** - Support for 30+ languages with native fluency

## 📁 Project Structure

```
tavus-demo/
├── app.py                    # Main entry point
├── config.py                 # Configuration and environment variables
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not in git)
├── .streamlit/
│   └── config.toml          # Streamlit theme configuration
├── pages/                    # Multi-page app structure
│   ├── 1_🏠_Home.py
│   ├── 2_📊_Analytics.py
│   ├── 3_⚡_Features.py
│   ├── 4_❓_FAQ.py
│   └── 5_📧_Contact.py
├── components/               # Reusable UI components
│   ├── __init__.py
│   ├── styles.py
│   ├── hero.py
│   └── cards.py
└── utils/                    # Business logic
    ├── __init__.py
    ├── api_client.py        # Tavus API interactions
    └── database.py          # Database operations
```

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Tavus API account and API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tavus-demo
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   API_KEY=your_tavus_api_key_here
   BROADGATE_PERSONA_ID=your_persona_id_here
   WEBHOOK_URL=your_webhook_url_here  # Optional
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The application will open in your browser at `http://localhost:8501`

## 🔧 Configuration

### Environment Variables

- `API_KEY` - Your Tavus API key (required)
- `BROADGATE_PERSONA_ID` - The persona ID for your AI agent (required)
- `WEBHOOK_URL` - Webhook URL for lead capture (optional)

### Customization

- **Branding**: Edit `config.py` to change brand name, colors, and other settings
- **Styling**: Modify `components/styles.py` for custom CSS
- **Pages**: Add new pages in the `pages/` directory following the naming convention

## 📊 Usage

### Navigation

The application uses Streamlit's multi-page architecture:
- **Home** - Main landing page with live demo
- **Analytics** - Real-time performance dashboard
- **Features** - Platform capabilities
- **FAQ** - Frequently asked questions
- **Contact** - Contact form

### Starting a Conversation

1. Navigate to the Home page
2. Click on the animated demo image
3. The AI voice agent will connect in a modal dialog
4. Have a natural conversation with the AI

## 🚀 Deployment

### Streamlit Community Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click "New app" and select your repository
4. Add your secrets in the Streamlit dashboard:
   ```toml
   API_KEY = "your_tavus_api_key"
   BROADGATE_PERSONA_ID = "your_persona_id"
   WEBHOOK_URL = "your_webhook_url"
   ```
5. Deploy!

### Other Platforms

The application can be deployed on any platform that supports Python and Streamlit:
- Railway
- Render
- AWS App Runner
- Google Cloud Run
- Heroku

## 🏗️ Architecture

### Modular Design

The codebase follows a modular architecture:

- **`config.py`** - Centralized configuration
- **`components/`** - Reusable UI components
- **`utils/`** - Business logic and API interactions
- **`pages/`** - Individual page modules

This structure ensures:
- Easy maintenance
- Code reusability
- Clear separation of concerns
- Scalability

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For support, email contact@voiceflow-ai.com or visit our website.

---

**VoiceFlow AI** - Intelligent Voice Automation Platform
