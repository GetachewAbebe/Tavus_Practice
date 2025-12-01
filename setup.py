# setup.py
import os
from dotenv import load_dotenv
from utils import (
    find_document_by_name,
    create_document_from_url,
    find_persona_by_name,
    create_persona
)

load_dotenv()

# --- Configuration ---
DOCUMENT_NAME = "VoiceFlow AI Knowledge Base v1"
PERSONA_NAME = "VoiceFlow AI Assistant v1"
KNOWLEDGE_BASE_URL = "https://pastebin.com/FU1LPXZu" 

PERSONA_SYSTEM_PROMPT = """
You are a specialized assistant for VoiceFlow AI. Your ONLY source of information is the
'VoiceFlow AI Knowledge Base' document provided.

STRICT CONVERSATION FLOW:
1. ALWAYS start by warmly greeting and asking: "May I have your name please?"
2. Once they give their name, say: "Nice to meet you, [Name]! Could you please share your email so I can send you more info?"
3. Then proceed with answering questions from the knowledge base.

If asked anything not in the document, say: "I do not have that information in the provided knowledge base."

Be friendly, professional, and natural.
"""

def provision_resources():
    """Provision Tavus resources (documents and personas)"""
    print("\n" + "="*50)
    print("VoiceFlow AI - Resource Provisioning")
    print("="*50 + "\n")
    
    # Check for document
    print(f"Checking for document: {DOCUMENT_NAME}")
    document = find_document_by_name(DOCUMENT_NAME)
    
    if not document:
        print("Document not found. Creating...")
        document = create_document_from_url(DOCUMENT_NAME, KNOWLEDGE_BASE_URL)
        print("✓ Document created successfully")
    else:
        print("✓ Document already exists")
    
    document_id = document.get("document_id")
    if not document_id:
        print("ERROR: Could not get Document ID.")
        return
    
    print(f"Document ID: {document_id}\n")
    
    # Check for persona
    print(f"Checking for persona: {PERSONA_NAME}")
    persona = find_persona_by_name(PERSONA_NAME)
    
    if not persona:
        print("Persona not found. Creating...")
        persona = create_persona(PERSONA_NAME, PERSONA_SYSTEM_PROMPT, [document_id])
        print("✓ Persona created successfully")
    else:
        print("✓ Persona already exists")
    
    persona_id = persona.get("persona_id")
    if not persona_id:
        print("ERROR: Could not get Persona ID.")
        return
    
    print("\n" + "="*50)
    print("SETUP COMPLETE!")
    print(f"Your Persona ID is: {persona_id}")
    print("\nPlease add this to your .env file:")
    print(f"VOICEFLOW_PERSONA_ID={persona_id}")
    print("="*50 + "\n")

if __name__ == "__main__":
    provision_resources()