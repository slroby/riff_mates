from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

def credits(request):
    content = "Nicky\nSean"

    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = "<p> You do the hokey pokey and you turn yourself around...</p>"

    return HttpResponse(content)

def version(request):
     content = {"version": "1.0"}
     
     return JsonResponse(content)

def news(request):
    data = {
        "news": ["RiffMates now has a news page!", "RiffMates has its first pages!"],
    }

    return render(request, "news2.html", data)

def news_advanced(request):
    data = {
        "news": [(datetime.fromisoformat('2024-03-16'), "RiffMates now has a news page!"), 
                 (datetime.fromisoformat('2024-03-15'), "RiffMates has its first pages!")],
    }

    print(data)
    return render(request, "news_adv.html", data)


print("http://127.0.0.1:8000/news/")
print("http://127.0.0.1:8000/news_advanced/")
print("http://127.0.0.1:8000/credits/")
print("http://127.0.0.1:8000/about/")
print("http://127.0.0.1:8000/version/")