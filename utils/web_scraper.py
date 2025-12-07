"""
Web scraper utility for extracting content from websites
"""

import requests
from bs4 import BeautifulSoup
from typing import Optional
import time


def scrape_website(url: str, max_retries: int = 3) -> Optional[str]:
    """
    Scrape text content from a website
    
    Args:
        url: The URL to scrape
        max_retries: Maximum number of retry attempts
        
    Returns:
        Extracted text content or None if failed
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
            
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                print(f"Failed to scrape {url} after {max_retries} attempts")
                return None
    
    return None


def scrape_multiple_pages(urls: list[str]) -> str:
    """
    Scrape multiple pages and combine their content
    
    Args:
        urls: List of URLs to scrape
        
    Returns:
        Combined text content from all pages
    """
    all_content = []
    
    for url in urls:
        print(f"Scraping: {url}")
        content = scrape_website(url)
        if content:
            all_content.append(f"=== Content from {url} ===\n\n{content}\n\n")
        else:
            print(f"Warning: Could not scrape {url}")
    
    return "\n".join(all_content)
