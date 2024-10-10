import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Find all headlines from the page according the the HTML header structure
    headlines = soup.find_all('h2')  #Adjust the tag to match the website's structure
    
    for idx, headline in enumerate(headlines[:5], start=1):
        print(f"{idx}. {headline.text.strip()}")

#Scrape headlines from cbsnews website (Only websites that allow scrapping)
url = "https://www.cbsnews.com/tag/bing/"
get_headlines(url)
