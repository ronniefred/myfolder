from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
page=None
def world(request):
    page ="Home page"
    page2 ="coding camp home page"
    age=18
    context = {
            "age" : age,
            "page" : page,
            "page" : page2,
    }
    return render (request, "file2/home.html",context)
def contact(request):
    return render (request, "file2/contact.html")
def about(request):
    return render (request, "file2/about.html")
def feedback(request):
    return render (request, "file2/feedback.html")