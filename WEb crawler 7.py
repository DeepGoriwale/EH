import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"
}


def get_html(url):
    try:
        return requests.get(url, headers=HEADERS).text
    except:
        return None


def get_robots(start_url):
    robots = RobotFileParser()
    robots_url = urljoin(start_url, "/robots.txt")
    try:
        robots.parse(requests.get(
            robots_url, headers=HEADERS).text.split("\n"))
    except:
        pass
    return robots


def extract_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    return [urljoin(base, a['href']) for a in soup.find_all('a', href=True)]


def crawl(url, max_depth=2, delay=1):
    visited = set()
    robots = get_robots(url)

    def go(link, depth):
        if depth > max_depth or link in visited:
            return
        if not robots.can_fetch("*", link):
            print(f"Blocked by robots.txt: {link}")
            return

        visited.add(link)
        time.sleep(delay)

        html = get_html(link)
        if html:
            print(f"Crawling {link}")
            for next_link in extract_links(html, link):
                go(next_link, depth + 1)

    go(url, 1)


# Example usage
print("Shani Mishra 31")
crawl("https://wikipedia.com", max_depth=2, delay=2)
