from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

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

    return render(request, "news.html", data)

print("http://127.0.0.1:8000/news/")
print("http://127.0.0.1:8000/credits/")
print("http://127.0.0.1:8000/about/")
print("http://127.0.0.1:8000/version/")