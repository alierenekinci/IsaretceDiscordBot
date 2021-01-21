import requests
from bs4 import BeautifulSoup
import discord
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def getData(text):

    link = "https://isaretce.com/?s=" + text
    site = requests.get(link, headers=headers)
    siteIcerigi = BeautifulSoup(site.content, "html5lib")

    if "Üzgünüz, ancak aradığınız kelimeyi bulamadık." in str(siteIcerigi):
        return ("0","0","0")
    else:
        title = siteIcerigi.find("h1", attrs={"class","entry-title"}).string
        gifLink = siteIcerigi.find("img", attrs={"class", "alignnone"}).get("src")
        #description = siteIcerigi.find("div", attrs={"class","column"}).string
    
        description = siteIcerigi.find_all("p")[-1].getText()

        return title, gifLink, description
