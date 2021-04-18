from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

def home(request):
    import requests 
    import json
    if request.method=='POST':
        query = request.POST['search']
        news_api_request = requests.get('https://newsapi.org/v2/everything?q='+query+'&from=2021-03-17&sortBy=publishedAt&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    else:
        news_api_request = requests.get('https://newsapi.org/v2/top-headlines?country=in&from=2021-03-17&sortBy=publishedAt&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    api = json.loads(news_api_request.content)
    return render(request,'home.html', {"api":api})
