from django.shortcuts import render
import requests
import os
api_key = os.getenv("NEWSAPI_KEY")

# Create your views here.

def index(request):
    url = 'https://newsapi.org/v2/everything?q=(football OR soccer) AND (EPL OR UEFA OR Premier League OR Barcelona OR Real Madrid)&sortBy=popularity&apiKey='+api_key
    response = requests.get(url).json()
    articles = response['articles']
    desc=[]
    title=[]
    img=[]
    for article in articles:
        title_text = article['title'] or ""
        
        if "football" in title_text.lower() or "soccer" in title_text.lower():
            title.append(article['title'])
            desc.append(article['description'])
            img.append(article['urlToImage'])
            
    mylist = list(zip(title, desc, img))
    return render(request, 'index.html', {"mylist": mylist})

    