"""
VoiceFlow AI - Styling Module
Custom CSS and theme management for the application
"""

import streamlit as st
from config import PRIMARY_COLOR, BACKGROUND_COLOR, SECONDARY_BG_COLOR, TEXT_COLOR


def apply_custom_css():
    """Apply custom CSS styling to the Streamlit application"""
    st.markdown(f"""
    <style>
        /* Global Styles */
        .stApp {{
            background: linear-gradient(135deg, {BACKGROUND_COLOR} 0%, #1a2332 100%);
        }}
        
        /* Header Styles */
        h1, h2, h3 {{
            color: {TEXT_COLOR};
            font-weight: 700;
        }}
        
        /* Button Styles */
        .stButton > button {{
            background: linear-gradient(135deg, {PRIMARY_COLOR} 0%, #2563EB 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3);
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4);
        }}
        
        /* Card Styles */
        .metric-card {{
            background: {SECONDARY_BG_COLOR};
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid #334155;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        /* Input Styles */
        .stTextInput > div > div > input {{
            background: {SECONDARY_BG_COLOR};
            border: 1px solid #334155;
            border-radius: 8px;
            color: {TEXT_COLOR};
        }}
        
        /* Sidebar Styles */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {SECONDARY_BG_COLOR} 0%, {BACKGROUND_COLOR} 100%);
        }}
        
        /* Status Badge */
        .status-badge {{
            display: inline-flex;
            align-items: center;
            padding: 0.5rem 1rem;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid #10B981;
            border-radius: 20px;
            color: #10B981;
            font-weight: 600;
            font-size: 0.875rem;
        }}
        
        /* Pulse Animation */
        @keyframes pulse {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.5;
            }}
        }}
        
        .pulse {{
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }}
        
        /* Modal Styles */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 1000;
        }}
        
        .modal-content {{
            background: {SECONDARY_BG_COLOR};
            border-radius: 16px;
            padding: 2rem;
            max-width: 600px;
            margin: 2rem auto;
            border: 1px solid #334155;
        }}
    </style>
    """, unsafe_allow_html=True)


def create_metric_card(title: str, value: str, icon: str = "📊") -> str:
    """Create a styled metric card HTML"""
    return f"""
    <div class="metric-card">
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
                <div style="color: #94A3B8; font-size: 0.875rem; margin-bottom: 0.5rem;">{title}</div>
                <div style="color: {TEXT_COLOR}; font-size: 2rem; font-weight: 700;">{value}</div>
            </div>
            <div style="font-size: 3rem; opacity: 0.5;">{icon}</div>
        </div>
    </div>
    """


def create_status_badge(status: str, color: str = "#10B981") -> str:
    """Create a styled status badge HTML"""
    return f"""
    <div class="status-badge" style="border-color: {color}; color: {color};">
        <span style="width: 8px; height: 8px; background: {color}; border-radius: 50%; margin-right: 8px; box-shadow: 0 0 8px {color};" class="pulse"></span>
        {status}
    </div>
    """
