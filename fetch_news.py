import feedparser
import json
import os
from datetime import datetime

# --- CONFIGURATION: Updated High-Signal, Live Business AI Feeds ---
FEEDS = {
    "AI News": "https://www.artificialintelligence-news.com/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "MIT Tech Review": "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/"
}

def fetch_boutique_news():
    combined_articles = []

    for source_name, url in FEEDS.items():
        print(f"Scanning {source_name}...")
        feed = feedparser.parse(url)
        
        for entry in feed.entries[:4]:  # Take the top 4 freshest items from each source
            # Smart image extraction logic across modern WordPress/Media platforms
            image_url = ""
            if 'media_content' in entry and len(entry.media_content) > 0:
                image_url = entry.media_content[0]['url']
            elif 'links' in entry:
                for link in entry.links:
                    if 'image' in link.get('type', ''):
                        image_url = link.href
            
            # Backup image extraction check if embedded inside extensions
            if not image_url and 'media_thumbnail' in entry and len(entry.media_thumbnail) > 0:
                image_url = entry.media_thumbnail[0]['url']

            article = {
                "title": entry.title,
                "url": entry.link,
                "urlToImage": image_url,
                "description": entry.get('summary', '')[:150] + "...",
                "source": source_name
            }
            combined_articles.append(article)

    # Compile and overwrite the news archive structure
    output = {
        "last_updated": datetime.now().strftime("%B %d, %Y"),
        "articles": combined_articles[:30]
    }

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
    
    print(f"Archive Refined: {output['last_updated']}")

if __name__ == "__main__":
    fetch_boutique_news()
