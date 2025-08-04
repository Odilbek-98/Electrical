from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request=request,template_name="index.html")

def about_page_view(request):
    return render(request=request,template_name="about.html")
