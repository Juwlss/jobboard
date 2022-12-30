from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('jobs.html',views.jobs, name='jobs'),
    path('candidate.html',views.candidate, name='candidate'),
    path('job_details.html',views.job_details, name='job_details'),
    path('elements.html',views.elements, name='elements'),
    path('blog.html',views.blog, name='blog'),
    path('single-blog.html',views.single_blog, name='single_blog'),
    path('contact.html',views.contact, name='contact'),
    path('<int:job_id>/', views.detail, name='detail'),
]
