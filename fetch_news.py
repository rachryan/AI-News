import requests
import os
import json

def fetch_ai_news():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print("Missing API Key")
        return

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence (tools OR productivity OR software)",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 6, 
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        new_articles = response.json().get('articles', [])

        # --- ARCHIVING LOGIC ---
        # 1. Load existing news if the file exists
        if os.path.exists("news.json"):
            with open("news.json", "r", encoding="utf-8") as f:
                try:
                    old_news = json.load(f)
                except json.JSONDecodeError:
                    old_news = []
        else:
            old_news = []

        # 2. Combine and remove duplicates based on URL
        existing_urls = {article['url'] for article in old_news}
        unique_new = [a for a in new_articles if a['url'] not in existing_urls and "Removed" not in a['title']]
        
        # 3. Keep the most recent 20 articles total
        combined_news = (unique_new + old_news)[:20]

        with open("news.json", "w", encoding="utf-8") as f:
            json.dump(combined_news, f, indent=4)
            
        print(f"Archived! {len(unique_new)} new articles added.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_ai_news()
