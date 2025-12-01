"""
VoiceFlow AI - Configuration Module
Centralized configuration and environment variable management
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Brand Configuration
BRAND_NAME = "VoiceFlow AI"
BRAND_TAGLINE = "Intelligent Voice Automation Platform"
BRAND_DOMAIN = "voiceflow-ai.com"

# API Configuration
TAVUS_API_KEY = os.getenv("API_KEY")
VOICEFLOW_PERSONA_ID = os.getenv("VOICEFLOW_PERSONA_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
REPLICA_ID = os.getenv("REPLICA_ID", "rfe12d8b9597")  # Default replica ID

# Database Configuration
DB_PATH = "voiceflow_leads.db"

# UI Configuration
PAGE_TITLE = f"{BRAND_NAME} | Enterprise Edition"
PAGE_ICON = "🎙️"
LAYOUT = "wide"

# Theme Colors
PRIMARY_COLOR = "#3B82F6"
BACKGROUND_COLOR = "#0F172A"
SECONDARY_BG_COLOR = "#1E293B"
TEXT_COLOR = "#F8FAFC"
