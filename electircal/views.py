from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Blog
from .models import Team


def home_page_view(request):
    return render(request=request,template_name="index.html")

def about_page_view(request):
    return render(request=request,template_name="about.html")

def service_page_view(request):
    return render(request=request,template_name="service.html")

def blog_page_view(request):
    context = {'blogs':Blog.objects.all().order_by("-created_date")}
    return render(request=request,template_name="blog.html",context=context)

def project_page_view(request):
    return render(request=request,template_name="project.html")

def team_page_view(request):
    context = {'teams':Team.objects.all().order_by()}
    return render(request=request,template_name="team.html")

def testimonial_page_view(request):
    return render(request=request,template_name="testimonial.html")

def contact_page_view(request):
    form = ContactForm(request.POST)
    if request.method == 'GET':
        return render(request=request,template_name="contact.html",context={'form': form})
    else:
        if form.is_valid():
            form.save() 
        return redirect('home-page')

