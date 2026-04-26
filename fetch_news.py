import requests
import os
import json

def fetch_ai_news():
    api_key = os.getenv("NEWS_API_KEY")
    
    if not api_key:
        print("Missing API Key")
        return

    # Specifically searching for tools, workflows, and stacks to fit your brand
    # language=en ensures no more foreign results
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence (tools OR stack OR productivity OR software)",
        "language": "en",
        "sortBy": "relevancy", # Relevancy often yields better quality than just "newest"
        "pageSize": 9,           # 9 articles fills a 3x3 grid perfectly
        "apiKey": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        # We filter out articles that are missing titles or links
        filtered_articles = [
            a for a in articles 
            if a.get('title') and a.get('url') and "Removed" not in a['title']
        ]

        with open("news.json", "w", encoding="utf-8") as f:
            json.dump(filtered_articles, f, indent=4)
            
        print(f"Success! {len(filtered_articles)} articles captured.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_ai_news()
