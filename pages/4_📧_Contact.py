"""
VoiceFlow AI - Contact Page
Contact form and support information
"""

import streamlit as st
from config import BRAND_NAME, PAGE_ICON
from components import apply_custom_css, render_sidebar, show_success_message

# Page configuration
st.set_page_config(
    page_title=f"{BRAND_NAME} | Contact",
    page_icon="📧",
    layout="wide"
)

# Apply styling and sidebar
apply_custom_css()
render_sidebar()

# Header
st.markdown("# 📧 Contact Us")
st.markdown("Get in touch with our team")
st.markdown("---")

# Contact Options
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 💬 Send Us a Message")
    
    with st.form("contact_form"):
        name = st.text_input("Name *", placeholder="Your full name")
        email = st.text_input("Email *", placeholder="your.email@example.com")
        company = st.text_input("Company", placeholder="Your company name")
        
        subject = st.selectbox(
            "Subject *",
            [
                "General Inquiry",
                "Technical Support",
                "Sales Question",
                "Partnership Opportunity",
                "Feature Request",
                "Bug Report",
                "Other"
            ]
        )
        
        message = st.text_area(
            "Message *",
            placeholder="Tell us how we can help you...",
            height=150
        )
        
        submitted = st.form_submit_button("Send Message", type="primary", use_container_width=True)
        
        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields (*)")
            else:
                # In a real application, this would send an email or save to a database
                show_success_message(f"Thank you, {name}! We've received your message and will get back to you soon.")
                st.balloons()

with col2:
    st.markdown("## 📍 Contact Information")
    
    st.markdown("""
    <div style="
        background: #1E293B;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #334155;
    ">
        <h4 style="color: #F8FAFC; margin-top: 0;">VoiceFlow AI</h4>
        
        <div style="margin: 1rem 0;">
            <div style="color: #94A3B8; font-size: 0.875rem;">Email</div>
            <div style="color: #F8FAFC;">support@voiceflow-ai.com</div>
        </div>
        
        <div style="margin: 1rem 0;">
            <div style="color: #94A3B8; font-size: 0.875rem;">Phone</div>
            <div style="color: #F8FAFC;">+1 (555) 123-4567</div>
        </div>
        
        <div style="margin: 1rem 0;">
            <div style="color: #94A3B8; font-size: 0.875rem;">Hours</div>
            <div style="color: #F8FAFC;">Mon-Fri: 9AM - 6PM EST</div>
        </div>
        
        <div style="margin: 1rem 0;">
            <div style="color: #94A3B8; font-size: 0.875rem;">Location</div>
            <div style="color: #F8FAFC;">San Francisco, CA</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🌐 Follow Us")
    st.markdown("""
    - [Twitter](https://twitter.com)
    - [LinkedIn](https://linkedin.com)
    - [GitHub](https://github.com)
    - [YouTube](https://youtube.com)
    """)

st.markdown("---")

# Support Resources
st.markdown("## 📚 Support Resources")

resource_col1, resource_col2, resource_col3 = st.columns(3)

with resource_col1:
    st.markdown("""
    ### 📖 Documentation
    Comprehensive guides and API references
    """)
    if st.button("View Docs", use_container_width=True):
        st.info("Documentation coming soon!")

with resource_col2:
    st.markdown("""
    ### ❓ FAQ
    Answers to frequently asked questions
    """)
    if st.button("Browse FAQ", use_container_width=True):
        st.switch_page("pages/3_❓_FAQ.py")

with resource_col3:
    st.markdown("""
    ### 💡 Community
    Join our community forum
    """)
    if st.button("Join Community", use_container_width=True):
        st.info("Community forum coming soon!")

st.markdown("---")

# Enterprise Support
st.markdown("## 🏢 Enterprise Support")

st.markdown("""
Looking for dedicated support for your organization? Our Enterprise plan includes:

- **Dedicated Account Manager** - Your personal point of contact
- **Priority Support** - 24/7 support with <1 hour response time
- **Custom SLA** - Tailored service level agreements
- **Technical Consultation** - Architecture and integration guidance
- **Training Sessions** - Onboarding and best practices training
- **Custom Development** - Bespoke features and integrations
""")

if st.button("Contact Sales for Enterprise", type="primary"):
    st.info("Our sales team will contact you within 24 hours!")

st.markdown("---")

# Office Hours
st.markdown("## 🕒 Office Hours")

st.markdown("""
Join our weekly office hours for live Q&A sessions:

**When:** Every Thursday at 2:00 PM EST  
**Where:** Virtual (Zoom link sent via email)  
**What:** Ask questions, get demos, discuss use cases

Register for the next session below:
""")

if st.button("Register for Office Hours", use_container_width=True):
    st.success("Registration link sent to your email!")
