"""
Broadgate - Modal Components
Modal dialogs for conversations and interactions
"""

import streamlit as st


def show_conversation_modal(conversation_url: str):
    """Display a modal with the conversation iframe"""
    if conversation_url:
        # Append parameters to hide local video and maximize AI
        # activeSpeakerMode=true: Focus on the speaker (usually AI)
        # showLocalVideo=0: Try to hide the user's self-view (best effort)
        # showParticipantsBar=0: Hide the sidebar
        # startVideoOff=1: Start with camera off
        # showUserName=0: Hide name tags
        separator = "&" if "?" in conversation_url else "?"
        final_url = f"{conversation_url}{separator}activeSpeakerMode=true&showLocalVideo=0&showParticipantsBar=0&startVideoOff=1&showUserName=0&showSelfView=0&showUserNames=0&showName=0&videoSource=false"

        st.markdown(f"""
        <div style="
            background: #1E293B;
            border-radius: 16px;
            padding: 2rem;
            border: 1px solid #334155;
            margin: 2rem 0;
        ">
            <h3 style="color: #F8FAFC; margin-bottom: 1rem;">🎙️ Live Conversation</h3>
            <iframe 
                src="{final_url}" 
                style="
                    width: 100%;
                    height: 600px;
                    border: none;
                    border-radius: 12px;
                "
                allow="microphone; camera"
            ></iframe>
            <div style="margin-top: 1rem; color: #94A3B8; font-size: 0.875rem;">
                💡 Allow microphone access when prompted to start the conversation
            </div>
        </div>
        """, unsafe_allow_html=True)


def show_info_modal(title: str, content: str, icon: str = "ℹ️"):
    """Display an informational modal"""
    st.markdown(f"""
    <div style="
        background: #1E293B;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #334155;
        margin: 1rem 0;
    ">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
            <h4 style="color: #F8FAFC; margin: 0;">{title}</h4>
        </div>
        <div style="color: #CBD5E1; line-height: 1.6;">
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_success_message(message: str):
    """Display a success message"""
    st.markdown(f"""
    <div style="
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid #10B981;
        border-radius: 8px;
        padding: 1rem;
        color: #10B981;
        margin: 1rem 0;
    ">
        <strong>✓ Success:</strong> {message}
    </div>
    """, unsafe_allow_html=True)


def show_error_message(message: str):
    """Display an error message"""
    st.markdown(f"""
    <div style="
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid #EF4444;
        border-radius: 8px;
        padding: 1rem;
        color: #EF4444;
        margin: 1rem 0;
    ">
        <strong>✗ Error:</strong> {message}
    </div>
    """, unsafe_allow_html=True)
