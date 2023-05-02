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

    #extract the title
    title = soup.find("title")
    if title is not None:
        print(f"Title: {title.text}\n")
    else:
        print('No title found')     
    
    # Extract the list of topics
    # print("Topics:")
    # topics = soup.find("ul", {"class": "list-row-container menu"})
    # for li in topics.find_all("li"):
    #     print(li.text.strip())

def extract_real_python_tutorials(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the list of tutorials
    print("List of tutorials:")
    latest_tutorials = soup.find("div", {"class": "card-deck"}).find_all("h2")
    print("Latest Tutorials:")
    for tutorial in latest_tutorials:
        print(tutorial.text.strip())




if __name__ == "__main__":
    urls = {"https://en.wikipedia.org/wiki/Python_(programming_language)": extract_python_org_info,
            "https://www.python.org/about/": extract_python_org_info,
            "https://realpython.com/": extract_real_python_tutorials,
            }
    for url, extraction_function in urls.items():
        print(f"Fetching information from: {url}\n")
        html_content = fetch_page(url)

        if html_content:
            extraction_function(html_content)
            print("\n" + "=" * 80 + "\n")
