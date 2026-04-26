import requests
import os
import json

def fetch_ai_news():
    # 1. Get the API Key from GitHub Secrets
    api_key = os.getenv("NEWS_API_KEY")
    
    if not api_key:
        print("Error: NEWS_API_KEY not found. Make sure it is set in GitHub Secrets.")
        return

    # 2. Define the search parameters
    # We focus on AI tools and tech stacks in English, sorted by newest
    query = "artificial intelligence AND (tools OR 'tech stack' OR software)"
    url = "https://newsapi.org/v2/everything"
    
    params = {
        "q": query,
        "language": "en",        # Strictly English news
        "sortBy": "publishedAt", # Get the latest updates
        "pageSize": 6,           # Top 6 articles for a clean grid
        "apiKey": api_key
    }

    try:
        print(f"Fetching news for TechTidy...")
        response = requests.get(url, params=params)
        response.raise_for_status() # Check for HTTP errors
        
        data = response.json()
        articles = data.get('articles', [])

        # 3. Save the results to news.json
        # This is the file your index.html reads from
        with open("news.json", "w", encoding="utf-8") as f:
            json.dump(articles, f, indent=4)
            
        print(f"Successfully saved {len(articles)} articles to news.json")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_ai_news()
