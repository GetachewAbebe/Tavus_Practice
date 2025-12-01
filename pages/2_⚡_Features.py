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
st.markdown("# ⚡ Platform Features")
st.markdown("Discover the powerful capabilities of VoiceFlow AI")
st.markdown("---")

# Core Features
st.markdown("## 🎯 Core Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🎙️ AI Voice Conversations
    Natural, context-aware voice interactions powered by advanced AI
    
    **Key Benefits:**
    - Real-time voice synthesis
    - Natural language understanding
    - Context retention across conversations
    - Multi-turn dialogue support
    """)
    
    st.markdown("""
    ### 📝 Knowledge Base Integration
    Connect your documentation and knowledge sources
    
    **Key Benefits:**
    - Document-based responses
    - Automatic knowledge extraction
    - Version control for knowledge bases
    - Multi-document support
    """)
    
    st.markdown("""
    ### 🔔 Webhook Notifications
    Real-time alerts and integrations
    
    **Key Benefits:**
    - Instant conversation notifications
    - Custom payload formatting
    - Retry logic for reliability
    - Multiple endpoint support
    """)

with col2:
    st.markdown("""
    ### 🎨 Custom Personas
    Create branded AI personalities
    
    **Key Benefits:**
    - Customizable system prompts
    - Brand voice alignment
    - Persona versioning
    - A/B testing support
    """)
    
    st.markdown("""
    ### 📊 Analytics & Insights
    Comprehensive conversation analytics
    
    **Key Benefits:**
    - Real-time metrics
    - Lead capture tracking
    - Conversion analytics
    - Export capabilities
    """)
    
    st.markdown("""
    ### 🔒 Enterprise Security
    Bank-grade security and compliance
    
    **Key Benefits:**
    - End-to-end encryption
    - SOC 2 compliance
    - GDPR ready
    - Data residency options
    """)

st.markdown("---")

# Advanced Capabilities
st.markdown("## 🚀 Advanced Capabilities")

tab1, tab2, tab3 = st.tabs(["🧠 AI Features", "🔗 Integrations", "📈 Scalability"])

with tab1:
    st.markdown("""
    ### Intelligent AI Capabilities
    
    #### Context-Aware Processing
    - Maintains conversation history
    - Understands user intent
    - Adapts responses based on context
    
    #### Natural Language Understanding
    - Multi-language support
    - Sentiment analysis
    - Entity extraction (names, emails, etc.)
    
    #### Smart Routing
    - Intent-based conversation flows
    - Dynamic response generation
    - Fallback handling
    
    #### Learning & Improvement
    - Conversation analysis
    - Performance optimization
    - Continuous model updates
    """)

with tab2:
    st.markdown("""
    ### Seamless Integrations
    
    #### CRM Integration
    - Salesforce
    - HubSpot
    - Pipedrive
    - Custom CRM via API
    
    #### Communication Platforms
    - Slack notifications
    - Microsoft Teams
    - Email automation
    - SMS alerts
    
    #### Analytics Tools
    - Google Analytics
    - Mixpanel
    - Segment
    - Custom analytics
    
    #### Development Tools
    - REST API
    - Webhooks
    - SDKs (Python, JavaScript)
    - GraphQL support
    """)

with tab3:
    st.markdown("""
    ### Enterprise-Grade Scalability
    
    #### Performance
    - 99.9% uptime SLA
    - <100ms response latency
    - Auto-scaling infrastructure
    - Global CDN distribution
    
    #### Capacity
    - Unlimited conversations
    - Concurrent call handling
    - High-volume support
    - Burst traffic management
    
    #### Reliability
    - Redundant systems
    - Automatic failover
    - Data backup & recovery
    - 24/7 monitoring
    
    #### Support
    - Dedicated account manager
    - Priority support queue
    - Custom SLA options
    - Technical consultation
    """)

st.markdown("---")

# Use Cases
st.markdown("## 💼 Use Cases")

use_case_col1, use_case_col2, use_case_col3 = st.columns(3)

with use_case_col1:
    st.markdown("""
    ### 📞 Customer Support
    - 24/7 availability
    - Instant responses
    - Escalation to humans
    - Multi-language support
    """)

with use_case_col2:
    st.markdown("""
    ### 🎯 Lead Generation
    - Qualify prospects
    - Capture contact info
    - Schedule meetings
    - CRM integration
    """)

with use_case_col3:
    st.markdown("""
    ### 📚 Information Desk
    - Answer FAQs
    - Product information
    - Navigation assistance
    - Document search
    """)

st.markdown("---")

# CTA
st.markdown("## 🚀 Ready to Experience These Features?")

cta_col1, cta_col2 = st.columns(2)

with cta_col1:
    if st.button("🎙️ Try Live Demo", type="primary", use_container_width=True):
        st.switch_page("app.py")

with cta_col2:
    if st.button("📧 Contact Sales", type="secondary", use_container_width=True):
        st.switch_page("pages/4_📧_Contact.py")
