"""
VoiceFlow AI - Features Page
Platform capabilities and feature showcase
"""

import streamlit as st
from config import BRAND_NAME, PAGE_ICON
from components import apply_custom_css, render_sidebar

# Page configuration
st.set_page_config(
    page_title=f"{BRAND_NAME} | Features",
    page_icon="⚡",
    layout="wide"
)

# Apply styling and sidebar
apply_custom_css()
render_sidebar()

# Header
st.markdown("# ⚡ What You Can Do")
st.markdown("See what VoiceFlow AI can help you with")
st.markdown("---")

# Core Features
st.markdown("## 🎯 Main Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎙️ Voice Conversations
    Talk with AI just like talking to a person
    
    - Works in real-time
    - Understands what you mean
    - Remembers your conversation
    - Handles back-and-forth naturally
    """)
    
    st.markdown("""
    ### 📝 Your Knowledge Base
    Connect your documents and information
    
    - Upload your files
    - AI learns from them
    - Gives accurate answers
    - Update anytime
    """)
    
    st.markdown("""
    ### 🔔 Get Notified
    Know when something happens
    
    - Instant alerts
    - Works with your tools
    - Never miss a call
    - Automatic updates
    """)

with col2:
    st.markdown("""
    ### 🎨 Make It Yours
    Customize how AI talks
    
    - Match your brand
    - Set the tone
    - Choose the style
    - Test different approaches
    """)
    
    st.markdown("""
    ### 📊 See Your Results
    Track what's happening
    
    - Live updates
    - See who called
    - Track success
    - Download reports
    """)
    
    st.markdown("""
    ### 🔒 Safe & Secure
    Your data is protected
    
    - Bank-level security
    - Privacy compliant
    - Data protection
    - Secure storage
    """)

st.markdown("---")

# Use Cases
st.markdown("## 💼 How People Use It")

use_case_col1, use_case_col2, use_case_col3 = st.columns(3)

with use_case_col1:
    st.markdown("""
    ### 📞 Customer Support
    - Available 24/7
    - Quick answers
    - Can transfer to humans
    - Works in many languages
    """)

with use_case_col2:
    st.markdown("""
    ### 🎯 Collect Leads
    - Find potential customers
    - Get contact info
    - Set up meetings
    - Save to your system
    """)

with use_case_col3:
    st.markdown("""
    ### 📚 Answer Questions
    - Handle FAQs
    - Share product info
    - Help with navigation
    - Search documents
    """)

st.markdown("---")

# CTA
st.markdown("## 🚀 Ready to Try?")

cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    if st.button("🎙️ Start Now", type="primary", use_container_width=True):
        st.switch_page("app.py")

with cta_col2:
    if st.button("📧 Need Help?", type="secondary", use_container_width=True):
        st.switch_page("pages/4_📧_Contact.py")
