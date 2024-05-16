import requests
from bs4 import BeautifulSoup

def crawl_ptt_subArticles(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        push_elements = soup.find_all("div", class_="yellow--text text--darken-2 e7-recommend-message")
        for element in push_elements:
            push_content = element.find("span")
            if push_content:
                push_content_text = push_content.text.strip()
                if push_content_text.startswith(":"):
                    push_content_text = push_content_text[1:].strip()
                if "imgur.com" in push_content_text:
                    break
                print(f"\n{push_content_text}\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# 示例用法
crawl_ptt_subArticles("https://www.pttweb.cc/bbs/Gossiping/M.1715869876.A.76E.html")
