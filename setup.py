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
DOCUMENT_NAME = "Broadgate Knowledge Base v1"
PERSONA_NAME = "Broadgate Assistant v1"

PERSONA_SYSTEM_PROMPT = """
You are Alex, a specialized assistant for Broadgate. Your ONLY source of information is the
'Broadgate Knowledge Base' document provided.

Your goal is to answer user questions accurately based ONLY on the provided document.
If the answer is not in the document, politely say you don't know.

Guidelines:
1. ALWAYS start the conversation by introducing yourself: "Hi! I'm Alex, your Broadgate assistant. How can I help you today?"
2. After they respond, ask: "May I have your name please?"
3. Once they give their name, say: "Nice to meet you, [Name]! Could you please share your email so I can send you more information?"
4. Then proceed with answering their questions from the knowledge base.

If asked anything not in the document, say: "I do not have that information in the provided knowledge base."

Be friendly, professional, and natural. Always remember you are Alex.
"""

def provision_resources():
    """Provision Tavus resources (documents and personas)"""
    print("\n" + "="*50)
    print("Broadgate - Resource Provisioning")
    print("="*50 + "\n")
    
    # Check for persona
    print(f"Checking for persona: {PERSONA_NAME}")
    persona = find_persona_by_name(PERSONA_NAME)
    
    if not persona:
        print("Persona not found. Creating...")
        # Create persona without documents (we inject context dynamically)
        persona = create_persona(PERSONA_NAME, PERSONA_SYSTEM_PROMPT, [])
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
    print(f"BROADGATE_PERSONA_ID={persona_id}")
    print("="*50 + "\n")

if __name__ == "__main__":
    provision_resources()