"""
VoiceFlow AI - FAQ Page
Frequently asked questions and help documentation
"""

import streamlit as st
from config import BRAND_NAME, PAGE_ICON
from components import apply_custom_css, render_sidebar

# Page configuration
st.set_page_config(
    page_title=f"{BRAND_NAME} | FAQ",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply styling and sidebar
apply_custom_css()
render_sidebar()

# Header
st.markdown("# ❓ Frequently Asked Questions")
st.markdown("Find answers to common questions about VoiceFlow AI")
st.markdown("---")

# Search
search = st.text_input("🔍 Search FAQs", placeholder="Type your question...")

# FAQ Categories
st.markdown("## 📚 Categories")

tab1, tab2, tab3, tab4 = st.tabs(["🚀 Getting Started", "💡 Features", "🔧 Technical", "💰 Pricing"])

with tab1:
    st.markdown("### Getting Started")
    
    with st.expander("❓ What is VoiceFlow AI?"):
        st.markdown("""
        VoiceFlow AI is an intelligent voice automation platform that enables businesses to create 
        natural, AI-powered voice conversations. Our platform combines advanced AI with easy-to-use 
        tools to help you automate customer interactions, capture leads, and provide 24/7 support.
        """)
    
    with st.expander("❓ How do I get started?"):
        st.markdown("""
        Getting started is easy:
        1. **Sign up** for an account
        2. **Configure** your environment variables (API keys)
        3. **Run** the setup script to create your persona
        4. **Start** your first conversation from the Home page
        
        Check our documentation for detailed setup instructions.
        """)
    
    with st.expander("❓ Do I need technical knowledge?"):
        st.markdown("""
        Basic technical knowledge is helpful but not required. Our platform is designed to be 
        user-friendly with:
        - Simple web interface
        - Step-by-step setup guides
        - Pre-configured templates
        - Comprehensive documentation
        
        For advanced customization, Python knowledge is beneficial.
        """)
    
    with st.expander("❓ What are the system requirements?"):
        st.markdown("""
        **Minimum Requirements:**
        - Python 3.8 or higher
        - Modern web browser (Chrome, Firefox, Safari, Edge)
        - Internet connection
        - Microphone for voice conversations
        
        **Recommended:**
        - Python 3.10+
        - 4GB RAM
        - Stable broadband connection
        """)

with tab2:
    st.markdown("### Features")
    
    with st.expander("❓ What can I do with VoiceFlow AI?"):
        st.markdown("""
        VoiceFlow AI enables you to:
        - Create AI-powered voice conversations
        - Capture leads automatically
        - Integrate with your CRM via webhooks
        - Analyze conversation performance
        - Customize AI personas
        - Build knowledge bases
        - Export conversation data
        """)
    
    with st.expander("❓ How does lead capture work?"):
        st.markdown("""
        Our AI automatically extracts information from conversations:
        1. The AI asks for name and email during the conversation
        2. Our extraction engine parses the transcript
        3. Data is saved to the local database
        4. Webhooks notify your systems in real-time
        5. View captured leads in the Analytics dashboard
        """)
    
    with st.expander("❓ Can I customize the AI persona?"):
        st.markdown("""
        Yes! You can fully customize your AI persona:
        - **System Prompt**: Define personality and behavior
        - **Knowledge Base**: Upload your own documents
        - **Voice**: Choose from available voice options
        - **Conversation Flow**: Design custom interaction patterns
        
        Edit the `setup.py` file to modify your persona configuration.
        """)
    
    with st.expander("❓ What languages are supported?"):
        st.markdown("""
        VoiceFlow AI supports multiple languages including:
        - English
        - Spanish
        - French
        - German
        - Portuguese
        - And many more...
        
        Contact us for specific language requirements.
        """)

with tab3:
    st.markdown("### Technical")
    
    with st.expander("❓ How do I set up environment variables?"):
        st.markdown("""
        Create a `.env` file in your project root with:
        
        ```
        API_KEY=your_tavus_api_key
        VOICEFLOW_PERSONA_ID=your_persona_id
        WEBHOOK_URL=https://your-webhook-endpoint.com
        REPLICA_ID=rfe12d8b9597
        ```
        
        Run `setup.py` to generate your persona ID if you don't have one.
        """)
    
    with st.expander("❓ How do webhooks work?"):
        st.markdown("""
        Webhooks send real-time notifications to your endpoint:
        
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
        
        Configure your webhook URL in the `.env` file.
        """)
    
    with st.expander("❓ Where is data stored?"):
        st.markdown("""
        Data is stored in two locations:
        1. **Local Database**: SQLite database (`voiceflow_leads.db`)
        2. **Tavus Cloud**: Conversation recordings and transcripts
        
        All data is encrypted and secure. You have full control over local data.
        """)
    
    with st.expander("❓ Can I integrate with my existing systems?"):
        st.markdown("""
        Yes! Integration options include:
        - **Webhooks**: Real-time HTTP notifications
        - **API**: Direct API access to conversation data
        - **Database**: Direct SQLite database access
        - **CSV Export**: Export data for external tools
        
        Check our API documentation for integration guides.
        """)

with tab4:
    st.markdown("### Pricing")
    
    with st.expander("❓ How much does it cost?"):
        st.markdown("""
        VoiceFlow AI uses Tavus API pricing:
        - Pay-as-you-go model
        - No upfront costs
        - Charged per conversation minute
        - Volume discounts available
        
        Contact Tavus for current pricing details.
        """)
    
    with st.expander("❓ Is there a free trial?"):
        st.markdown("""
        Yes! Tavus offers:
        - Free API credits for new users
        - Test conversations included
        - No credit card required to start
        
        Sign up at tavus.io to get started.
        """)
    
    with st.expander("❓ What's included in the platform?"):
        st.markdown("""
        The VoiceFlow AI platform includes:
        - ✅ Unlimited personas
        - ✅ Knowledge base management
        - ✅ Analytics dashboard
        - ✅ Webhook integrations
        - ✅ Data export
        - ✅ Local database
        - ✅ Open-source code
        
        Conversation costs are based on Tavus API usage.
        """)

st.markdown("---")

# Still have questions?
st.markdown("## 💬 Still Have Questions?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📧 Contact Support
    Can't find what you're looking for? Our team is here to help!
    """)
    if st.button("Contact Us", type="primary", use_container_width=True):
        st.switch_page("pages/4_📧_Contact.py")

with col2:
    st.markdown("""
    ### 📚 Documentation
    Explore our comprehensive documentation and guides.
    """)
    if st.button("View Docs", type="secondary", use_container_width=True):
        st.info("Documentation coming soon!")
