"""
VoiceFlow AI - Webhook Module
Webhook integration and notification handling
"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def send_to_webhook(conv_id: str, name: str = None, email: str = None, transcript_text: str = ""):
    """Send lead data to webhook endpoint"""
    url = os.getenv("WEBHOOK_URL")
    
    if not url:
        print("WEBHOOK_URL not configured, skipping webhook")
        return
    
    payload = {
        "conversation_id": conv_id,
        "name": name or "",
        "email": email or "",
        "transcript": transcript_text,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        print(f"✓ Webhook sent successfully: {payload}")
        return True
    except requests.exceptions.Timeout:
        print(f"✗ Webhook timeout for conversation {conv_id}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"✗ Webhook failed: {e}")
        return False
