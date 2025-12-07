"""
Test script to verify website scraping functionality
"""

from utils.web_scraper import scrape_website

print("Testing website scraping...")
print("=" * 50)

url = "https://broadgatevoice.co.uk/"
content = scrape_website(url)

if content and len(content) > 100:
    print(f"✓ SUCCESS - Scraped {len(content)} characters")
    print("\nContent preview (first 300 characters):")
    print("-" * 50)
    print(content[:300])
    print("-" * 50)
else:
    print("✗ FAILED - Could not scrape website")
    print(f"Content: {content}")
