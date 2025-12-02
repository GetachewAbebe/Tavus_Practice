"""
VoiceFlow AI - Configuration Module
Centralized configuration and environment variable management
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Helper function to get config values from Streamlit secrets or environment variables
def get_config(key: str, default=None):
    """Get configuration value from Streamlit secrets or environment variables"""
    try:
        import streamlit as st
        # Try Streamlit secrets first (for cloud deployment)
        if hasattr(st, 'secrets') and key in st.secrets:
            return st.secrets[key]
    except (ImportError, FileNotFoundError, KeyError):
        pass
    
    # Fall back to environment variables (for local development)
    return os.getenv(key, default)

# Brand Configuration
BRAND_NAME = "VoiceFlow AI"
BRAND_TAGLINE = "Intelligent Voice Automation Platform"
BRAND_DOMAIN = "voiceflow-ai.com"

# API Configuration
TAVUS_API_KEY = get_config("API_KEY")
VOICEFLOW_PERSONA_ID = get_config("VOICEFLOW_PERSONA_ID")
WEBHOOK_URL = get_config("WEBHOOK_URL")
REPLICA_ID = get_config("REPLICA_ID", "rfe12d8b9597")  # Default replica ID

# Database Configuration
DB_PATH = "voiceflow_leads.db"

# UI Configuration
PAGE_TITLE = f"{BRAND_NAME} | Enterprise Edition"
PAGE_ICON = "🎙️"
LAYOUT = "wide"

# Theme Colors
PRIMARY_COLOR = "#3B82F6"
BACKGROUND_COLOR = "#FFFFFF"
SECONDARY_BG_COLOR = "#F8FAFC"
TEXT_COLOR = "#1E293B"
