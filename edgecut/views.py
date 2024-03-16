from django.shortcuts import render
def index(request):
    return render(request,"edgecut/index.html")
def about(request):
    return render(request,"edgecut/about.html")
def furniture(request):
    return render(request,"edgecut/furniture.html")
def blog(request):
    return render(request,"edgecut/blog.html")
def contact(request):
    return render(request,"edgecut/contact.html")
