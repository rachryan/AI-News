import feedparser
import json
import os
from datetime import datetime

# --- CONFIGURATION: Add your favorite high-signal RSS feeds here ---
FEEDS = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "Anthropic": "https://www.anthropic.com/news/rss",
    "Google AI": "https://blog.google/technology/ai/rss/",
    "MIT Tech Review": "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
    "The Verge AI": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml"
}

def fetch_boutique_news():
    combined_articles = []

    for source_name, url in FEEDS.items():
        print(f"Scanning {source_name}...")
        feed = feedparser.parse(url)
        
        for entry in feed.entries[:3]:  # Take the top 3 from each source
            # Extract image if available (logic varies by feed)
            image_url = ""
            if 'media_content' in entry:
                image_url = entry.media_content[0]['url']
            elif 'links' in entry:
                for link in entry.links:
                    if 'image' in link.get('type', ''):
                        image_url = link.href

            article = {
                "title": entry.title,
                "url": entry.link,
                "urlToImage": image_url,
                "description": entry.get('summary', '')[:150] + "...",
                "source": source_name
            }
            combined_articles.append(article)

    # Sort by date (if available) and limit to 30 for the archive
    output = {
        "last_updated": datetime.now().strftime("%B %d, %Y"),
        "articles": combined_articles[:30]
    }

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
    
    print(f"Archive Refined: {output['last_updated']}")

if __name__ == "__main__":
    fetch_boutique_news()
