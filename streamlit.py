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
    page_title=f"{BRAND_NAME}",
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
# {PAGE_ICON} {BRAND_NAME}

Talk to our AI assistant
""")

st.markdown("---")

# Demo Section
col_demo1, col_demo2 = st.columns([3, 1])

with col_demo1:
    if not st.session_state.call_url:
        # Advanced Settings Expander
        with st.expander("⚙️ Advanced Settings", expanded=False):
            st.markdown("**Optional Configuration**")
            
            test_mode = st.checkbox(
                "🧪 Test Mode (No Costs)", 
                value=False,
                help="Creates conversation without replica joining. No costs incurred, status will be 'ended'."
            )
            
            custom_persona = st.text_input(
                "Persona ID",
                value="",
                placeholder=VOICEFLOW_PERSONA_ID or "Default persona",
                help="Override the default persona ID"
            )
            
            custom_replica = st.text_input(
                "Replica ID",
                value="",
                placeholder="Default replica",
                help="Override the default replica ID"
            )
            
            custom_callback = st.text_input(
                "Callback URL",
                value="",
                placeholder=WEBHOOK_URL or "None",
                help="Webhook URL for conversation events"
            )
        
        if st.button("🎙️ Start Conversation", type="primary", use_container_width=True):
            if not VOICEFLOW_PERSONA_ID and not custom_persona:
                show_error_message("Setup needed. Contact support.")
            else:
                try:
                    with st.spinner("Getting ready..."):
                        result = create_conversation(
                            persona_id=custom_persona or VOICEFLOW_PERSONA_ID,
                            replica_id=custom_replica or None,
                            callback_url=custom_callback or WEBHOOK_URL,
                            test_mode=test_mode
                        )
                        st.session_state.call_url = result.get("conversation_url")
                        st.session_state.conversation_id = result.get("conversation_id")
                        
                        if test_mode:
                            show_success_message("Test conversation created! (No costs)")
                        else:
                            show_success_message("Ready!")
                        st.rerun()
                except Exception as e:
                    show_error_message(f"Error: {str(e)}")
    else:
        if st.button("🛑 End Call", type="secondary", use_container_width=True):
            try:
                if st.session_state.conversation_id:
                    end_conversation(st.session_state.conversation_id)
                st.session_state.call_url = None
                st.session_state.conversation_id = None
                show_success_message("Call ended")
                st.rerun()
            except Exception as e:
                show_error_message(f"Error: {str(e)}")

with col_demo2:
    st.markdown("""
    **Steps:**
    1. Click button
    2. Allow mic
    3. Start talking
    """)

# Display conversation iframe
if st.session_state.call_url:
    show_conversation_modal(st.session_state.call_url)