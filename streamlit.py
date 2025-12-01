"""
VoiceFlow AI - Main Application Entry Point
Enterprise Voice Automation Platform
"""
import streamlit as st
from config import PAGE_TITLE, PAGE_ICON, LAYOUT, BRAND_NAME
from components import apply_custom_css

# Page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# Apply custom styling
apply_custom_css()

# Initialize session state
if "call_url" not in st.session_state:
    st.session_state.call_url = None
if "show_modal" not in st.session_state:
    st.session_state.show_modal = False

# Sidebar branding
with st.sidebar:
    st.markdown(f"## {PAGE_ICON} {BRAND_NAME}")
    st.caption("Enterprise Edition v2.1")
    st.markdown("---")
    st.markdown("""
    <div style="background: #0F172A; padding: 1rem; border-radius: 8px; border: 1px solid #334155;">
        <div style="color: #94A3B8; font-size: 0.8rem; margin-bottom: 0.5rem;">SYSTEM STATUS</div>
        <div style="display: flex; align-items: center; color: #10B981; font-weight: 600; font-size: 0.9rem;">
            <span style="width: 8px; height: 8px; background: #10B981; border-radius: 50%; margin-right: 8px; box-shadow: 0 0 8px #10B981;"></span>
            Operational
        </div>
    </div>
    """, unsafe_allow_html=True)
# Main content
st.markdown("""
# Welcome to VoiceFlow AI
This is a modular, multi-page Streamlit application. Use the sidebar to navigate between pages.
**Available Pages:**
- 🏠 **Home** - Main landing page with live demo
- 📊 **Analytics** - Real-time performance dashboard
- ⚡ **Features** - Platform capabilities
- ❓ **FAQ** - Frequently asked questions
- 📧 **Contact** - Get in touch with our team
Navigate using the sidebar menu above.
""")
st.info("💡 **Tip**: This application now uses Streamlit's multi-page architecture for better organization and scalability.")