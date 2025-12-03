"""
Broadgate - Database Module
SQLite database operations for lead management
"""

import sqlite3
from datetime import datetime
from config import DB_PATH


def init_db():
    """Initialize the database with auto-migration"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conv_id TEXT,
            name TEXT,
            email TEXT
        )
    """)
    
    # Auto-migrate: add timestamp column if missing
    cur.execute("PRAGMA table_info(leads)")
    cols = [c[1] for c in cur.fetchall()]
    if 'ts' not in cols:
        cur.execute("ALTER TABLE leads ADD COLUMN ts TEXT")
    
    conn.commit()
    conn.close()


def save_lead(conv_id: str, name: str = None, email: str = None):
    """Save a lead to the database"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute(
        "INSERT INTO leads (conv_id, name, email, ts) VALUES (?, ?, ?, ?)",
        (conv_id, name, email, datetime.utcnow().isoformat())
    )
    
    conn.commit()
    conn.close()


def get_all_leads():
    """Get all leads from the database"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute("SELECT id, conv_id, name, email, ts FROM leads ORDER BY ts DESC")
    leads = cur.fetchall()
    
    conn.close()
    
    return [
        {
            "id": lead[0],
            "conv_id": lead[1],
            "name": lead[2],
            "email": lead[3],
            "timestamp": lead[4]
        }
        for lead in leads
    ]


def get_lead_count():
    """Get the total number of leads"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM leads")
    count = cur.fetchone()[0]
    
    conn.close()
    return count


def get_leads_by_date_range(start_date: str = None, end_date: str = None):
    """Get leads within a date range"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    if start_date and end_date:
        cur.execute(
            "SELECT id, conv_id, name, email, ts FROM leads WHERE ts BETWEEN ? AND ? ORDER BY ts DESC",
            (start_date, end_date)
        )
    else:
        cur.execute("SELECT id, conv_id, name, email, ts FROM leads ORDER BY ts DESC")
    
    leads = cur.fetchall()
    conn.close()
    
    return [
        {
            "id": lead[0],
            "conv_id": lead[1],
            "name": lead[2],
            "email": lead[3],
            "timestamp": lead[4]
        }
        for lead in leads
    ]
