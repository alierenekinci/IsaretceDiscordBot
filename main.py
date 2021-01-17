import requests
from bs4 import BeautifulSoup
import discord


def getData(text):

    link = "https://isaretce.com/?s=" + text
    site = requests.get(link)
    siteIcerigi = BeautifulSoup(site.content, "html5lib")

    if "Üzgünüz, ancak aradığınız kelimeyi bulamadık." in str(siteIcerigi):
        return ("0","0","0")
    else:
        title = siteIcerigi.find("h1", attrs={"class","entry-title"}).string
        gifLink = siteIcerigi.find("img", attrs={"class", "alignnone"}).get("src")
        #description = siteIcerigi.find("div", attrs={"class","column"}).string
    
        description = siteIcerigi.find_all("p")[-1].getText()

        return title, gifLink, description
