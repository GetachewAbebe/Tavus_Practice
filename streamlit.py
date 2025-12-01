"""
VoiceFlow AI - Home Page
Main landing page with live demo
"""

import streamlit as st
from config import BRAND_NAME, PAGE_ICON, VOICEFLOW_PERSONA_ID, WEBHOOK_URL
from components import apply_custom_css, render_sidebar, show_conversation_modal, show_error_message, show_success_message
from utils import create_conversation, end_conversation, init_db

# Page configuration
st.set_page_config(
    page_title=f"{BRAND_NAME} | Home",
    page_icon=PAGE_ICON,
    layout="wide"
)

# Apply styling and sidebar
apply_custom_css()
render_sidebar()

# Initialize database
init_db()

# Initialize session state
if "call_url" not in st.session_state:
    st.session_state.call_url = None
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

# Hero Section
st.markdown(f"""
# {PAGE_ICON} Welcome to {BRAND_NAME}

### Intelligent Voice Automation Platform

Transform your customer interactions with AI-powered voice conversations that feel natural, 
intelligent, and engaging.
""")

st.markdown("---")

# Features Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎯 Smart Conversations
    AI-powered personas that understand context and provide intelligent responses
    """)

with col2:
    st.markdown("""
    ### 📊 Real-time Analytics
    Track performance metrics and conversation insights in real-time
    """)

with col3:
    st.markdown("""
    ### 🔗 Seamless Integration
    Easy integration with your existing workflows via webhooks and APIs
    """)

st.markdown("---")

# Live Demo Section
st.markdown("## 🎙️ Try Our Live Demo")
st.markdown("Experience the power of AI voice conversations firsthand.")

col_demo1, col_demo2 = st.columns([2, 1])

with col_demo1:
    if not st.session_state.call_url:
        if st.button("🚀 Start Conversation", type="primary", use_container_width=True):
            if not VOICEFLOW_PERSONA_ID:
                show_error_message("Persona ID not configured. Please run setup.py first.")
            else:
                try:
                    with st.spinner("Initializing conversation..."):
                        result = create_conversation(
                            persona_id=VOICEFLOW_PERSONA_ID,
                            callback_url=WEBHOOK_URL
                        )
                        st.session_state.call_url = result.get("conversation_url")
                        st.session_state.conversation_id = result.get("conversation_id")
                        show_success_message("Conversation started successfully!")
                        st.rerun()
                except Exception as e:
                    show_error_message(f"Failed to start conversation: {str(e)}")
    else:
        if st.button("🛑 End Conversation", type="secondary", use_container_width=True):
            try:
                if st.session_state.conversation_id:
                    end_conversation(st.session_state.conversation_id)
                st.session_state.call_url = None
                st.session_state.conversation_id = None
                show_success_message("Conversation ended successfully!")
                st.rerun()
            except Exception as e:
                show_error_message(f"Failed to end conversation: {str(e)}")

with col_demo2:
    st.markdown("""
    **How it works:**
    1. Click "Start Conversation"
    2. Allow microphone access
    3. Start talking naturally
    4. AI responds in real-time
    """)

# Display conversation iframe
if st.session_state.call_url:
    show_conversation_modal(st.session_state.call_url)

st.markdown("---")

# Benefits Section
st.markdown("## 💡 Why Choose VoiceFlow AI?")

col_b1, col_b2 = st.columns(2)

with col_b1:
    st.markdown("""
    ### Enterprise-Grade Features
    - 🔒 **Secure & Compliant** - Enterprise-level security
    - 🌍 **Multi-language Support** - Communicate globally
    - 📈 **Scalable Infrastructure** - Grows with your needs
    - 🎨 **Customizable Personas** - Tailor to your brand
    """)

with col_b2:
    st.markdown("""
    ### Advanced Capabilities
    - 🧠 **Context-Aware AI** - Understands conversation flow
    - 📝 **Automatic Transcription** - Full conversation logs
    - 🔔 **Real-time Notifications** - Instant webhook alerts
    - 📊 **Detailed Analytics** - Actionable insights
    """)

st.markdown("---")

# CTA Section
st.markdown("## 🚀 Ready to Get Started?")
st.markdown("Explore our platform features or contact us for a custom demo.")

cta_col1, cta_col2, cta_col3 = st.columns(3)

with cta_col1:
    if st.button("📊 View Analytics", use_container_width=True):
        st.switch_page("pages/1_📊_Analytics.py")

with cta_col2:
    if st.button("⚡ Explore Features", use_container_width=True):
        st.switch_page("pages/2_⚡_Features.py")

with cta_col3:
    if st.button("📧 Contact Us", use_container_width=True):
        st.switch_page("pages/4_📧_Contact.py")