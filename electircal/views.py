from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request=request,template_name="index.html")

def about_page_view(request):
    return render(request=request,template_name="about.html")

def service_page_view(request):
    return render(request=request,template_name="service.html")

def blog_page_view(request):
    return render(request=request,template_name="blog.html")

def project_page_view(request):
    return render(request=request,template_name="project.html")

def team_page_view(request):
    return render(request=request,template_name="team.html")

def testimonial_page_view(request):
    return render(request=request,template_name="testimonial.html")

def contact_page_view(request):
    return render(request=request,template_name="contact.html") 