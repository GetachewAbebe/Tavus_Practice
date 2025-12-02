"""
VoiceFlow AI - Analytics Dashboard
Real-time performance metrics and conversation insights
"""

import streamlit as st
from datetime import datetime, timedelta
from config import BRAND_NAME, PAGE_ICON
from components import apply_custom_css, render_sidebar
from components.styling import create_metric_card
from utils import init_db, get_all_leads, get_lead_count

# Page configuration
st.set_page_config(
    page_title=f"{BRAND_NAME} | Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply styling and sidebar
apply_custom_css()
render_sidebar()

# Initialize database
init_db()

# Header
st.markdown("# 📊 Your Stats")
st.markdown("See how your conversations are performing")
st.markdown("---")

# Get data
leads = get_all_leads()
total_leads = get_lead_count()

# Calculate metrics
leads_with_email = sum(1 for lead in leads if lead.get('email'))
leads_with_name = sum(1 for lead in leads if lead.get('name'))
conversion_rate = (leads_with_email / total_leads * 100) if total_leads > 0 else 0

# Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("Total Calls", str(total_leads), "💬"), unsafe_allow_html=True)

with col2:
    st.markdown(create_metric_card("Emails Collected", str(leads_with_email), "✉️"), unsafe_allow_html=True)

with col3:
    st.markdown(create_metric_card("Success Rate", f"{conversion_rate:.1f}%", "📈"), unsafe_allow_html=True)

with col4:
    st.markdown(create_metric_card("Names Collected", str(leads_with_name), "👤"), unsafe_allow_html=True)

st.markdown("---")

# Recent Conversations
st.markdown("## 📋 Recent Calls")

if leads:
    # Display leads in a table
    for lead in leads[:10]:  # Show last 10
        col_id, col_name, col_email, col_time = st.columns([1, 2, 3, 2])
        
        with col_id:
            st.markdown(f"**#{lead['id']}**")
        
        with col_name:
            st.markdown(f"👤 {lead['name'] or 'Not provided'}")
        
        with col_email:
            st.markdown(f"✉️ {lead['email'] or 'Not provided'}")
        
        with col_time:
            if lead['timestamp']:
                try:
                    dt = datetime.fromisoformat(lead['timestamp'])
                    st.markdown(f"🕒 {dt.strftime('%Y-%m-%d %H:%M')}")
                except:
                    st.markdown(f"🕒 {lead['timestamp']}")
            else:
                st.markdown("🕒 N/A")
        
        st.markdown("---")
    
    if len(leads) > 10:
        st.info(f"Showing 10 of {len(leads)} total calls")
else:
    st.info("No calls yet. Start a conversation from the Home page to see stats here.")

st.markdown("---")

# Performance Insights
st.markdown("## 💡 Quick Tips")

col_insight1, col_insight2 = st.columns(2)

with col_insight1:
    st.markdown("""
    ### 🎯 What to Track
    - How many people share their email
    - Which conversations work best
    - When people call most often
    """)

with col_insight2:
    st.markdown("""
    ### 📈 Goals to Aim For
    - Get emails from 50%+ of calls
    - Keep improving your AI's responses
    - Test different conversation styles
    """)

# Export functionality
st.markdown("---")
st.markdown("## 📥 Download Your Data")

if st.button("📄 Download as Spreadsheet", type="secondary"):
    if leads:
        import csv
        from io import StringIO
        
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=['id', 'conv_id', 'name', 'email', 'timestamp'])
        writer.writeheader()
        writer.writerows(leads)
        
        st.download_button(
            label="⬇️ Download Now",
            data=output.getvalue(),
            file_name=f"voiceflow_calls_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    else:
        st.warning("No data to download yet")
