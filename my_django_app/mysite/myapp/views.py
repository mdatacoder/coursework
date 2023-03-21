from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = "<html>"\
        "This is my first view"\
        "</html>"
        
    return HttpResponse(content=template)
