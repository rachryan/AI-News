import requests
import os
import json
from datetime import datetime

def fetch_ai_news():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print("NEWS_API_KEY missing.")
        return

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence (tools OR workflow OR software)",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10, 
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        new_articles = response.json().get('articles', [])

        if os.path.exists("news.json"):
            with open("news.json", "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    old_news = data.get('articles', []) if isinstance(data, dict) else data
                except:
                    old_news = []
        else:
            old_news = []

        existing_urls = {article['url'] for article in old_news}
        unique_new = [a for a in new_articles if a['url'] not in existing_urls and "Removed" not in a['title']]
        
        # Keep 24 articles for the deep archive
        combined_news = (unique_new + old_news)[:24]

        output = {
            "last_updated": datetime.now().strftime("%d %b %Y").upper(),
            "articles": combined_news
        }

        with open("news.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)
            
        print(f"System Updated: {output['last_updated']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_ai_news()
