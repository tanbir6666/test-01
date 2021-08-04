import pandas as pd
import requests
from bs4 import BeautifulSoup

katmovieHD = requests.get("https://katmoviehd.si/one-wild-moment-2015/")


movie_info = BeautifulSoup(katmovieHD.content,"html.parser")

rating = movie_info.find_all(class_="entry-content")
#print(rating)

def p(print_element):
    print(print_element)


p(len(rating))
link_name=[]
link_adress=[]
list_items=rating[0].find_all("h2")
for lists in list_items:
    list_item_text= lists.find_all("a")
    for links in list_item_text:
        link_inside_text= links.get_text()
        p(link_inside_text)
        link_name.append(link_inside_text)
        p(links)
        link_adress.append(str(links))
        p("==============================")
    

all_links= pd.DataFrame({
    "link Name": link_name,
    "link": link_adress
})
all_links.to_csv("Tom and jerry.csv")
print(all_links)


# //////////succeed


