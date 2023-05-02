import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Error: Unable to fetch the page. Status code: {response.status_code}')
        return None


def extract_python_info(html_content):
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

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    html_content = fetch_page(url)
    
    if html_content:
        extract_python_info(html_content)
