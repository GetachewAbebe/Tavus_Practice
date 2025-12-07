"""
Broadgate - Utils Module
Utility functions for API, database, webhooks, and data extraction
"""

from .api import (
    find_document_by_name,
    create_document_from_url,
    find_persona_by_name,
    create_persona,
    create_conversation,
    end_conversation,
    get_conversation_messages
)

from .database import (
    init_db,
    save_lead,
    get_all_leads,
    get_lead_count
)

from .webhook import (
    send_to_webhook
)

from .extraction import (
    extract_transcript_text,
    extract_name,
    extract_email,
    extract_info_and_send_webhook
)

from .web_scraper import (
    scrape_website,
    scrape_multiple_pages
)

__all__ = [
    # API functions
    'find_document_by_name',
    'create_document_from_url',
    'find_persona_by_name',
    'create_persona',
    'create_conversation',
    'end_conversation',
    'get_conversation_messages',
    
    # Database functions
    'init_db',
    'save_lead',
    'get_all_leads',
    'get_lead_count',
    
    # Webhook functions
    'send_to_webhook',
    
    # Extraction functions
    'extract_transcript_text',
    'extract_name',
    'extract_email',
    'extract_info_and_send_webhook',
    
    # Web scraper functions
    'scrape_website',
    'scrape_multiple_pages'
]
