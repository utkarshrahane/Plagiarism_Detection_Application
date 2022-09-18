import requests
from bs4 import BeautifulSoup as bs
import warnings
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

warnings.filterwarnings("ignore", module='bs4')

#Search function
#The function is used for searching the content over the web.

def searchBing(query, num):

    #URL strutcure for searching over Microsoft Bing search engine.
    
    urls1 = []

    url1 = 'https://www.bing.com/search?q=' + query
    page = requests.get(url1, headers = {'User-agent': 'Mighty Near'})
    soup = bs(page.text, 'html.parser')
    
    for link in soup.find_all('a'):
        url1 = str(link.get('href'))
        if url1.startswith('http'):
            if not url1.startswith('https://go.m') and not url1.startswith('https://go.m'):
                urls1.append(url1)

    return urls1[:num]

def searchGoogle(query, num):

    urls2 = []

    url2 = 'https://www.google.com/search?q=' + query
    page = requests.get(url2, headers = {'User-agent': 'John Doe'})
    soup = bs(page.text, 'html.parser')

    for link in soup.find_all('a'):
        url2 = str(link.get('href'))
        if url2.startswith('http'):
            if not url2.startswith('https://go.m') and not url2.startswith('https://go.m') and not url2.startswith('https://maps.google'):
                urls2.append(url2)
    
    return urls2[:num]
    

#Extract Text function
#The function is used for extracting the relevant text from the web. 

def extractText(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    return soup.get_text()
    
