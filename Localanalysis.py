import requests
from bs4 import BeautifulSoup
from datetime import datetime
import openai

# --- CONFIGURATION ---
openai.api_key = 'your-openai-api-key'  # Replace with your actual OpenAI API key

# --- 1. Scrape News Articles from Debate Los Mochis ---
def scrape_los_mochis_news():
    url = 'https://www.debate.com.mx/los-mochis-t640615'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for article in soup.find_all('article')[:5]:  # Limit to top 5 for demo
        title = article.find('h2') or article.find('h3')
        summary = article.find('p')
        link_tag = article.find('a')

        if title and link_tag:
            title_text = title.get_text(strip=True)
            summary_text = summary.get_text(strip=True) if summary else "No summary available"
            link = link_tag['href']
            if not link.startswith("http"):
                link = f"https://www.debate.com.mx{link}"
            articles.append({
                'title': title_text,
                'summary': summary_text,
                'link': link,
                'date': datetime.now().strftime('%Y-%m-%d')
            })

    return articles

# --- 2. Format for GPT Prompt ---
def format_news_for_prompt(articles):
    return "\n\n".join([
        f"Title: {a['title']}\nSummary: {a['summary']}\nLink: {a['link']}"
        for a in articles
    ])

# --- 3. Ask GPT for Insights ---
def ask_chatgpt_for_insights(formatted_news):
    prompt = f"""
You are a business consultant. Here are today's news headlines from Los Mochis, Sinaloa:

{formatted_news}

Based on this, provide actionable business insights using this format:
- [Category] | Insight | Suggested Action
(Include Real Estate, Agriculture, Manufacturing, Consumer Trends, Public Policy)
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# --- MAIN RUN ---
def run_news_analysis():
    print("\n🔍 Scraping articles...")
    articles = scrape_los_mochis_news()
    if not articles:
        print("No articles found. Try again later.")
        return

    formatted_news = format_news_for_prompt(articles)
    print("\n💬 Asking ChatGPT for insights...")
    insights = ask_chatgpt_for_insights(formatted_news)

    print("\n📈 Business Insights from Los Mochis News:\n")
    print(insights)

# --- Execute when run directly ---
if __name__ == '__main__':
    run_news_analysis()
