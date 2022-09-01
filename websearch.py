import requests
from bs4 import BeautifulSoup as bs
import warnings

warnings.filterwarnings("ignore", module='bs4')

#Search function
#The function is used for searching the content over the web.

def searchBing(query, num):

    #URL strutcure for searching over Microsoft Bing search engine.
    url = 'https://www.bing.com/search?q=' + query
    urls = []

    page = requests.get(url, headers = {'User-agent': 'John Doe'})
    soup = bs(page.text, 'html.parser')

    for link in soup.find_all('a'):
        url = str(link.get('href'))
        if url.startswith('http'):
            if not url.startswith('http://go.m') and not url.startswith('https://go.m'):
                urls.append(url)
    
    return urls[:num]

#Extract Text function
#The function is used for extracting the relevant text from the web. 

def extractText(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup.get_text()
    
