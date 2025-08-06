from django.urls import path
from .views import home_page_view, about_page_view, service_page_view, blog_page_view, project_page_view, team_page_view, testimonial_page_view, contact_page_view
urlpatterns = [
    path('',home_page_view,name='home-page'),
    path('about/',about_page_view,name='about-page'),
    path('service/',service_page_view,name='service-page'),
    path('blog/',blog_page_view,name='blog-page'),
    path('project/',project_page_view,name='project-page'),
    path('team/',team_page_view,name='team-page'),
    path('testimonial/',testimonial_page_view,name='testimonial-page'),
    path('contact/',contact_page_view,name='contact-page'),
]