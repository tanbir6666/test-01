# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://facebook.com")

# soup = BeautifulSoup(page.content, "html.parser")


def p(ele):
    print(ele)


# p(soup)


def gap():
    p("=====================")
    p("=====================")
    p("=====================")


# gap()
# p(soup.find_all("a"))
# gap()
# all_targets = soup.find_all(id="post-99264")
# p(all_targets)

# gap()

# soup.find_all(class_='post_author')


# IMG = soup.find_all("li")
# print(IMG)

import pandas
import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup

TargetSite = requests.get("https://www.timeanddate.com/weather/bangladesh/dhaka/ext")

Now_what_to_suck = BeautifulSoup(TargetSite.content, "html.parser")
# p(Now_what_to_suck)

class_tb_scroll = Now_what_to_suck.find_all("tbody")
p(len(class_tb_scroll))
table_row=class_tb_scroll[0].find_all("tr")

p(len(table_row))


table_data={
    "table_header":[],
    "table_d":[]

}


for each_table_row in table_row:
    th = each_table_row.find_all("th")
    td = each_table_row.find_all("td")
    #print(th[0].get_text())
    table_datas=[]
    table_data["table_header"].append(th[0].get_text())

    for each_td in td:
        td_text = each_td.get_text()
        #print(td_text)
        table_datas.append(td_text)
    
    table_data["table_d"].append(table_datas)

def loopinDic():
        for theader in table_data["table_header"]:
            for tdatas in table_data["table_d"]:
                for tdatasX in tdatas:
                    print(theader, tdatasX)


table_d2 = table_data["table_d"][0:15]


def print_table():
            weather_work=pandas.DataFrame(
                {
                    "day": table_data["table_header"],
                 
                    "des2": table_d2,
                }
            )
            print(weather_work)
            weather_work.to_csv("weather.csv")


p(len(table_data["table_d"][0]))
print_table()
