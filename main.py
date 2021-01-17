import requests
from bs4 import BeautifulSoup


def sorgu(text):

    link = "https://isaretce.com/?s=" + text
    site = requests.get(link)
    siteIcerigi = BeautifulSoup(site.content, "html5lib")
    if "Üzgünüz, ancak aradığınız kelimeyi bulamadık." in str(siteIcerigi):
        return "Üzgünüz, ancak aradığınız kelimeyi bulamadık."
    else:
        title = siteIcerigi.find("h1", attrs={"class","entry-title"}).string
        gifLink = siteIcerigi.find("img", attrs={"class", "alignnone"}).get("src")
        vs = siteIcerigi.find_all("p")[-1].getText()

        return title, gifLink, vs
text = input()
text.replace()
