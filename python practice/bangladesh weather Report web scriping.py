import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as BuS


page = rq.get("https://www.apunkagames.biz/2020/12/cyberpunk-2077-game.html")

get_page=BuS(page.content,"html.parser")


TodayWeather = get_page.find(class_="bb_ul")

TodayWeather_li = TodayWeather.find_all("li")

#print(get_page.prettify())
xh=0
print(get_page.status_code)
for gh in TodayWeather_li:
   
    for_p= gh.get_text()

    print(xh, "/ " ,for_p)
   
    
    xh+=1

#print(list(get_page.children))






if TodayWeather:
        print(True)
else:

        print(False)


def printBy():
    for weather in TodayWeather:
        
        weather_string = weather.get_text()
    
        main_weather = int(weather_string)
        print(main_weather)

