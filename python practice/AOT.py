import requests as rq
from bs4 import BeautifulSoup as Bu
import pandas as pd
page_link=rq.get("https://attacktitanepisodes.com/")
page=Bu(page_link.content,"html.parser")
links_table=page.find_all("table")
#print(links_table)


links=[]
links_title=[]
for lin in links_table:
	td=lin.find_all("td")
	print(td)
	for tabsx in td:
		print(tabsx)
		print("=============")
		try:
			print("tryied")
			link_a= tabsx.select("a")
			print(link_a)
			print("after link_A printed")
			href=link_a[0].get("href")
			title=link_a[0].get_text()
			links_title.append(title)
			links.append(href)
		except:
		    a=0

#print(links)
table_data=pd.DataFrame({
	"Title":links_title,
	"links":links
	})
print(table_data)
table_data.to_csv("AOT.csv")