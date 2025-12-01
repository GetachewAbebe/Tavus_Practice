"""
VoiceFlow AI - Sidebar Component
Reusable sidebar with branding and system status
"""

import streamlit as st
from config import BRAND_NAME, PAGE_ICON


def render_sidebar():
    """Render the application sidebar with branding and status"""
    with st.sidebar:
        # Branding
        st.markdown(f"## {PAGE_ICON} {BRAND_NAME}")
        st.caption("Enterprise Edition v2.1")
        st.markdown("---")
        
        # System Status
        st.markdown("""
        <div style="background: #0F172A; padding: 1rem; border-radius: 8px; border: 1px solid #334155;">
            <div style="color: #94A3B8; font-size: 0.8rem; margin-bottom: 0.5rem;">SYSTEM STATUS</div>
            <div style="display: flex; align-items: center; color: #10B981; font-weight: 600; font-size: 0.9rem;">
                <span style="width: 8px; height: 8px; background: #10B981; border-radius: 50%; margin-right: 8px; box-shadow: 0 0 8px #10B981;"></span>
                Operational
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation Info
        st.markdown("### 📍 Navigation")
        st.markdown("""
        - 🏠 **Home** - Live Demo
        - 📊 **Analytics** - Metrics
        - ⚡ **Features** - Capabilities
        - ❓ **FAQ** - Help
        - 📧 **Contact** - Support
        """)
        
        st.markdown("---")
        
        # Footer
        st.caption("© 2024 VoiceFlow AI")
        st.caption("All rights reserved")
