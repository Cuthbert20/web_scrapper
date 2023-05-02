import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Error: Unable to fetch the page. Status code: {response.status_code}')
        return None

#info from wiki
def extract_wiki_python_info(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the summary paragraph
    summary = soup.find("div", {"id": "bodyContent"}).find("p")
    print(f"Summary:\n{summary.text}\n")
    
    # Extract the table of contents
    toc = soup.find("div", {"id": "toc"})
    if toc is not None:
        print("Table of Contents:")
        for item in toc.find_all("li"):
            print(item.text)
    else:
        print('No table of contents found')

#info from python.org
def extract_python_org_info(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the heading
    heading = soup.find("h1", {"class": "page-title"}).text.strip()
    print(f"Heading: {heading}\n")
    
    # Extract the summary paragraph
    summary = soup.find("div", {"class": "introduction"}).text.strip()
    print(f"Summary:\n{summary}\n")
    
    # Extract the list of topics
    print("Topics:")
    topics = soup.find("ul", {"class": "list-row-container menu"})
    for li in topics.find_all("li"):
        print(li.text.strip())


if __name__ == "__main__":
    urls = {"https://en.wikipedia.org/wiki/Python_(programming_language)": extract_python_org_info,
            "https://www.python.org/about/": extract_python_org_info
            }
    html_content = fetch_page(url)
    
    if html_content:
        extract_wiki_python_info(html_content)
