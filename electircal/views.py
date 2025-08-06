from django.shortcuts import render,redirect
from .forms import ContactForm
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
    if request.method == 'GET':
        form = ContactForm(request.POST)
        return render(request=request,template_name="contact.html",context={'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # phone_number = form.cleaned_data['phone_number']
            # project = form.cleaned_data['project']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']
            form.save() 
        return redirect('home-page')

