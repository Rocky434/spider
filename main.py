import requests
from bs4 import BeautifulSoup
import foo
def crawl_ptt_articles(url, max_articles=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    articles_found = 0
    while articles_found < max_articles:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        for entry in soup.find_all("div", class_="e7-right-top-container e7-no-outline-all-descendants"):
            article_url = "https://www.pttweb.cc" + entry.find('a').get("href")
            foo.crawl_ptt_subArticles(article_url)
            articles_found += 1
            if articles_found >= max_articles:
                break
        
        prev_page = soup.find("a", string="‹ 上頁")
        if prev_page:
            url = "https://www.pttweb.cc" + prev_page["href"]
        else:
            break

if __name__ == "__main__":
    crawl_ptt_articles("https://www.pttweb.cc/hot/all/today", max_articles=10)
