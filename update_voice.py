
import os
import sys
from config import BROADGATE_PERSONA_ID, TTS_ENGINE, BRITISH_VOICE_ID
from utils.api import update_persona_voice

def main():
    print(f"Updating Persona: {BROADGATE_PERSONA_ID}")
    print(f"TTS Engine: {TTS_ENGINE}")
    print(f"Voice ID: {BRITISH_VOICE_ID}")
    
    if not BROADGATE_PERSONA_ID:
        print("Error: BROADGATE_PERSONA_ID is not set.")
        return

    try:
        response = update_persona_voice(BROADGATE_PERSONA_ID, TTS_ENGINE, BRITISH_VOICE_ID)
        print("Success! Persona updated.")
        print(response)
    except Exception as e:
        print(f"Error updating persona: {e}")
        # If 'add' failed, maybe try 'replace' manually if needed, but let's see the error first.

if __name__ == "__main__":
    main()
