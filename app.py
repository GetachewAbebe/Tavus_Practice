"""
Broadgate - Home Page
Main landing page with live demo
"""

import os
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Broadgate",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from config import BRAND_NAME, PAGE_ICON, BROADGATE_PERSONA_ID, WEBHOOK_URL
from components import apply_custom_css, render_sidebar, show_conversation_modal, show_error_message, show_success_message
from utils import create_conversation, end_conversation, init_db
from utils.pdf_processor import extract_text_from_pdf, find_pdf_in_dir

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
                "🧪 Connection Test (No AI)", 
                value=False,
                help="Checks connection only. The AI will NOT join. To talk to the AI, uncheck this."
            )
            
            custom_persona = st.text_input(
                "Persona ID",
                value="",
                placeholder=BROADGATE_PERSONA_ID or "Default persona",
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

            custom_greeting = st.text_input(
                "Custom Greeting (Speak First)",
                value="Hello! I'm your AI assistant. How can I help you today?",
                help="The AI will speak this message immediately when the conversation starts."
            )
        
        if st.button("🎙️ Start Conversation", type="primary", use_container_width=True):
            if not BROADGATE_PERSONA_ID and not custom_persona:
                show_error_message("Setup needed. Contact support.")
            else:
                try:
                    # Clear any existing session state to prevent 404 errors on restart
                    st.session_state.call_url = None
                    st.session_state.conversation_id = None
                    
                    with st.spinner("Getting ready..."):
                        # Check for PDF knowledge base
                        context_text = None
                        # Try specific path first, then root
                        pdf_path = None
                        specific_path = os.path.join("Konwledge_Base", "Broadgate.pdf")
                        if os.path.exists(specific_path):
                            pdf_path = specific_path
                        else:
                            pdf_path = find_pdf_in_dir(".")
                            
                        if pdf_path:
                            try:
                                context_text = extract_text_from_pdf(pdf_path)
                                st.toast(f"Loaded knowledge base from {os.path.basename(pdf_path)}", icon="📚")
                            except Exception as e:
                                st.warning(f"Could not load PDF: {e}")

                        result = create_conversation(
                            persona_id=custom_persona or BROADGATE_PERSONA_ID,
                            replica_id=custom_replica or None,
                            callback_url=custom_callback or WEBHOOK_URL,
                            test_mode=test_mode,
                            custom_greeting=custom_greeting,
                            context_text=context_text
                        )
                        
                        # Validate response before setting session state
                        if not result or not result.get("conversation_url"):
                            raise ValueError("Invalid API response - no conversation URL received")
                        
                        st.session_state.call_url = result.get("conversation_url")
                        st.session_state.conversation_id = result.get("conversation_id")
                        
                        if test_mode:
                            show_success_message("Connection test started (AI will not join)")
                        else:
                            show_success_message("Ready!")
                        st.rerun()
                except Exception as e:
                    # Clear session state on error to prevent stale URLs
                    st.session_state.call_url = None
                    st.session_state.conversation_id = None
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