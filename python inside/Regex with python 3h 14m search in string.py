# Real expresson

from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
import re

text = "e A random String"

pattern = re.compile("A random String")

result = pattern.search(text)
# search() function will be off after it finds the very first match


print(result)

# to find a single letter

pattern_single = re.compile("[ABCejhdsafcbksadfcjasdn]")
# this will look for any Single A,B or C
result_of_single = pattern_single.search(text)
# search function will be off after it finds the very first match

print(result_of_single)

# in pattern_single=re.compile("[abcdefghijklmnopqrstwxyz]")
# can be write line this pattern_single=re.compile("[a-z]")

Alphabets = "a , b , c , d , e , f , g , h"

find_Alphabets = re.compile("[a-zA-Z]")

result_of_finding_alphabets = find_Alphabets.search(Alphabets)
print(result_of_finding_alphabets)
Alphabets.upper()
upperAlphabets = Alphabets.upper()
new_text = "hello world"
# with re.compile("[a-zA-Z]+") "+" is new: we can

find_Alphabets2 = re.compile("[a-zA-Z]+")
result_of_finding_alphabets2 = find_Alphabets2.search(new_text)
print(result_of_finding_alphabets2)

# lets find an email from a string

myself = "hi I am Tanbir, I am 21 years old and My email address is tanbirhawlader12690@gmail.com & The New Email address is tanbirhawlader126900@gmail.com , tan#bir$hawl&ader12_6900@gmail.com"

# email has always @ in it. so that's  the target

email_pattern = re.compile(
    "[a-zA-Z0-9\.\@\#\$\%\^\&\*\_\-]+@+[a-zA-Z0-9\.\@\#\$\%\^\&\*\_\-]+")
# [a-zA-Z0-9.]+@+[a-zA-Z0-9.]+ means a to z OR A to Z OR 0 to 9 Or '.'-dot + @+ a-z A-z 0-9 and dot(.)

result_of_email = email_pattern.search(myself)
print(result_of_email)
find_all_email = email_pattern.findall(myself)
print(find_all_email)


with_html_tag = ["<a href=\"https://fast.com \">Download Now </a> ",
                 "<a href=\"https://fast.com \">Download Now </a> ", "<a href=\"https://fast.com \">Download Now </a> ", "<a href=\"https://fast.com \">Fast.com</a>"]


page_request = rq.get(
    "https://vegamovies.pw/download-king-kong-2005-dual-audio-hindi-english-movie-480p-720p-1080p/")
page_data = BeautifulSoup(page_request.content, "html.parser")

page_a_links = page_data.find_all("a")
for l in page_a_links:
    if l.find_all(class_="dwd-button"):
       link_btns = l.find_all(class_="dwd-button")
       btn_inside_text=  link_btns[0].get_text()
       link_btn = l.get("href")
       print(btn_inside_text)
       print(link_btn)


def ano():
        Download_pattern = re.compile(
            "[a-zA-Z0-9\.\<\>\@\$\&\*\(\)\+\_\=\ \-\%\~\`\"\'\:\;\/]+Download+[a-zA-Z0-9\.\<\>\@\$\&\*\(\)\+\_\=\-\%\~\`\"\'\:\;\ \/\</]+")
        tagsLink = []
        indexs=0
        for tags in all_ancore_tags:

            #print(tags)
            All_download_links = Download_pattern.findall(tags.get_text())
            if Download_pattern.findall(tags.get_text()):
                print(tags.get_text())
                print(tags.get("href"))
                print("===================================================================")
                print(All_download_links)
                indexs+=1
            else:
                print("===================Not Matched==================")
                print(tags.get_text())
                btns=tags.find_all("button")
                if tags.find_all("button"):
                    print("++++++++++++++++++++++++++++++|||||||||btn found|||||||++++++++++++++++++++++++++++++++++++++")
                print(btns)
                print(tags.get("href"))
                print(tags)
                print("===================Not Matched==================")







































def unKnown():

                result_download_links = Download_pattern.findall(tags)
                if Download_pattern.findall(tags):
                    tagsLink.append(result_download_links)
                print("]]]=================[[[[[[[[[[")
                print(result_download_links)


                print(tagsLink)

                all_download_link_names = []
                all_download_address = []
                if len(tagsLink) > 0:
                    for link_number in tagsLink:
                        print(link_number[0])
                        # link_names = link_number[0].get_text()
                        # link_address = link_number[0].get("href")
                        # all_download_link_names.append(link_names)
                        # all_download_address.append(link_address)


                data_table = pd.DataFrame({
                    "Download Name": all_download_link_names,
                    "Download Links": all_download_address

                })
                print(data_table)
