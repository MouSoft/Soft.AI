
import feedparser

def fetch_google_news(query='أخبار'):
    feed_url = f"https://news.google.com/rss/search?q={query}&hl=ar&gl=SA&ceid=SA:ar"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries[:10]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        })
    return articles
