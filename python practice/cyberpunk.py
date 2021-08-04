import pandas
import requests as rq
from bs4 import BeautifulSoup


def requestFunction(page_link):
    page_to_get = rq.get(page_link)
    all_html_data_inside_the_page=BeautifulSoup(page_to_get.content,"html.parser")
    









page_link = rq.get("https://www.apunkasoftware.net/vlink/10092627767")

page_link_data=BeautifulSoup(page_link.content,"html.parser")

donwload_links =page_link_data.find_all("form")
download_cyberpunk_links=[]
download_cyberpunk_links_name=[]
for each_form in donwload_links:
    links_= each_form.select("input[name=file]")
    links_value = links_[0].get("value")


    download_cyberpunk_links.append(links_value)


    linksName=each_form.select("input[type=submit]")
    linksNameValue = linksName[0].get("value")
    download_cyberpunk_links_name.append(linksNameValue)




listXL=pandas.DataFrame({
    "Link Name": download_cyberpunk_links_name,
    "Link": download_cyberpunk_links,
})
listXL.to_csv("Horizon Zero Dawn links.csv")
print(listXL)
print("done")


