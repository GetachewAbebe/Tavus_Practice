"""
VoiceFlow AI - API Client
Functions for interacting with the Tavus API
"""

import requests
from config import TAVUS_API_KEY


def _headers():
    """Get API headers with authentication"""
    if not TAVUS_API_KEY:
        raise ValueError("API_KEY missing. Please configure it in Streamlit Cloud secrets or .env file")
    return {"x-api-key": TAVUS_API_KEY}


# ========== Documents ==========

def find_document_by_name(name: str):
    """Find a document by name"""
    r = requests.get("https://tavusapi.com/v2/documents", headers=_headers())
    r.raise_for_status()
    for d in r.json().get("data", []):
        if d.get("document_name") == name:
            return d
    return None


def create_document_from_url(name: str, url: str):
    """Create a new document from a URL"""
    payload = {"document_name": name, "document_url": url}
    r = requests.post("https://tavusapi.com/v2/documents", json=payload, headers=_headers())
    r.raise_for_status()
    return r.json()


# ========== Personas ==========

def find_persona_by_name(name: str):
    """Find a persona by name"""
    r = requests.get("https://tavusapi.com/v2/personas", headers=_headers())
    r.raise_for_status()
    for p in r.json().get("data", []):
        if p.get("persona_name") == name:
            return p
    return None


def create_persona(name: str, system_prompt: str, document_ids: list):
    """Create a new persona with system prompt and documents"""
    payload = {
        "pipeline_mode": "full",
        "persona_name": name,
        "system_prompt": system_prompt,
        "document_ids": document_ids,
    }
    r = requests.post("https://tavusapi.com/v2/personas", json=payload, headers=_headers())
    r.raise_for_status()
    return r.json()


# ========== Conversations ==========

def create_conversation(persona_id: str, replica_id: str = None, callback_url: str = None, test_mode: bool = False):
    """Create a new conversation with a persona
    
    Args:
        persona_id: ID of the persona to use
        replica_id: ID of the replica (defaults to config REPLICA_ID)
        callback_url: Optional webhook URL for conversation events
        test_mode: If True, creates conversation without replica joining (no costs)
    """
    from config import REPLICA_ID
    
    if replica_id is None:
        replica_id = REPLICA_ID
    
    payload = {"persona_id": persona_id, "replica_id": replica_id}
    if callback_url:
        payload["callback_url"] = callback_url
    if test_mode:
        payload["test_mode"] = test_mode
    
    r = requests.post("https://tavusapi.com/v2/conversations", json=payload, headers=_headers())
    r.raise_for_status()
    return r.json()


def end_conversation(conv_id: str):
    """End an active conversation"""
    if not conv_id:
        raise ValueError("conv_id required")
    
    r = requests.post(f"https://tavusapi.com/v2/conversations/{conv_id}/end", headers=_headers())
    r.raise_for_status()
    
    # Check if the response has content and is JSON before trying to parse
    if r.status_code == 200 and r.headers.get('Content-Type', '').startswith('application/json'):
        return r.json()
    
    return {"status": "success", "message": "Conversation ended"}


def get_conversation_messages(conv_id: str):
    """Get all messages from a conversation"""
    if not conv_id:
        return []
    
    r = requests.get(f"https://tavusapi.com/v2/conversations/{conv_id}/messages", headers=_headers())
    
    if r.status_code == 404:
        return []
    
    r.raise_for_status()
    data = r.json()
    return data.get("data", data if isinstance(data, list) else [])
