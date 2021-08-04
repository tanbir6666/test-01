import pandas
import requests
from bs4 import BeautifulSoup

kat = requests.get("https://katmoviehd.si/category/adult/page/2/")
#https://katmoviehd.si/category/adult/page/2/
get_page=BeautifulSoup(kat.content,"html.parser")


get_all_a_tag = get_page.find_all("a")
all_link_name=[]
all_links_=[]
for links in get_all_a_tag:
    all_link_name.append(links.get_text())
    all_links_.append(str(links.get("href")))


data= pandas.DataFrame({
    "Link Names": all_link_name,
    "Links": all_links_
})

data.to_csv("KatmovieHD Links on first_page date 25 feb 2021.csv")
