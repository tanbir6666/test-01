from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bs4 import BeautifulSoup as Bu
import  requests as rq
import re
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.

links=""

elements={
    "poster":[],
    "link":[],
    "links_text":[]
}



link_thumbnail = []



def home(request):
    global links, link_thumbnail, elements
    return render(request, "search/search.html", {"links": links, "thumbnail": elements})
    link_thumbnail=[]
    

@csrf_exempt
def getElements(request):
    global links, link_thumbnail, elements
    try:
        search_text = request.POST["s"]
        search_texts = str(search_text)

        page = rq.get("https://katmoviehd.si/?s="+search_texts+"")
        page_elements = Bu(page.content,"html.parser")
        print(page_elements)
        search_pattern = re.compile(
            "[a-zA-Z0-9\/\:\;\+\-\_\^\%\$\#\@\!\~\.\=]+https://+[a-zA-Z0-9\/\:\;\+\-\_\^\%\$\#\@\!\~\.\=]")

        #links = search_pattern.findall(page_elements)
        links = page_elements.find_all(class_="type-post")

        #poster
        for th in links:
            thumblesOf = th.find_all(class_="Thumbnail")
            link_th = thumblesOf[0].get("src")
            elements["poster"].append(str(link_th))
        #links
        for eachhref in links:
            linksOf = eachhref.find_all("a")
            linksHref = linksOf[1].get("href")
            elements["link"].append(str(linksHref))

            link_text = linksOf[1].get_text()
            elements["links_text"].append(str(link_text))
            


        print("COMPILE LINKS ===============-------------------------------------------------------------==")
        print("COMPILE LINKS ===============-------------------------------------------------------------==")
        #print(links)
        print("COMPILE LINKS ===============-------------------------------------------------------------==")
        print("COMPILE LINKS ===============-------------------------------------------------------------==")
   
        return HttpResponseRedirect("/search/")




    except:
        print("UNABLE TO PROCESS //////////////....................///////////////////////............./////////////")
        return HttpResponseRedirect("/search/")
