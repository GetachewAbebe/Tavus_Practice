"""
VoiceFlow AI - Data Extraction Module
Extract information from conversation transcripts
"""

import re
from .api import get_conversation_messages
from .webhook import send_to_webhook
from .database import save_lead


def extract_transcript_text(conv_id: str) -> str:
    """
    Extract transcript text from conversation messages.
    Returns a single string containing all message text.
    """
    messages = get_conversation_messages(conv_id)
    
    if not messages:
        return ""
    
    transcript_parts = []
    for msg in messages:
        # Try different possible keys for message text
        text = (
            msg.get("text") or 
            msg.get("content") or 
            msg.get("message") or 
            msg.get("transcript") or
            ""
        )
        if text:
            transcript_parts.append(str(text))
    
    return "\n".join(transcript_parts)


def extract_name(transcript_text: str) -> str:
    """Extract name from transcript using regex patterns"""
    if not transcript_text:
        return None
    
    # Pattern 1: "My name is [Name]"
    pattern1 = re.search(r"(?:my name is|i'm|i am)\s+([a-zA-Z\s]+)", transcript_text, re.IGNORECASE)
    if pattern1:
        return pattern1.group(1).strip()
    
    # Pattern 2: "This is [Name]"
    pattern2 = re.search(r"(?:this is|call me)\s+([a-zA-Z\s]+)", transcript_text, re.IGNORECASE)
    if pattern2:
        return pattern2.group(1).strip()
    
    return None


def extract_email(transcript_text: str) -> str:
    """Extract email from transcript using regex"""
    if not transcript_text:
        return None
    
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", transcript_text)
    
    if email_match:
        return email_match.group(0)
    
    return None


def extract_info_and_send_webhook(conv_id: str):
    """
    Extract name and email from conversation transcript,
    then send to webhook and save to database
    """
    if not conv_id:
        print("No conversation ID provided for webhook processing.")
        return
    
    # Extract transcript
    transcript_text = extract_transcript_text(conv_id)
    
    # Extract information
    name = extract_name(transcript_text)
    email = extract_email(transcript_text)
    
    print(f"Extracted from conversation {conv_id}:")
    print(f"  Name: {name or 'Not found'}")
    print(f"  Email: {email or 'Not found'}")
    
    # Send to webhook
    send_to_webhook(conv_id, name, email, transcript_text)
    
    # Save to database
    save_lead(conv_id, name, email)
    
    return {
        "name": name,
        "email": email,
        "transcript": transcript_text
    }
