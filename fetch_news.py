import requests
import os

def fetch_ai_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=artificial+intelligence&sortBy=publishedAt&apiKey={api_key}"
    
    response = requests.get(url)
    articles = response.json().get('articles', [])[:5] # Get top 5
    
    # Format the data for your website
    with open("news.json", "w") as f:
        import json
        json.dump(articles, f)

if __name__ == "__main__":
    fetch_ai_news()
