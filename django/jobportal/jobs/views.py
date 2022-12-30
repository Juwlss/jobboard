from django.shortcuts import render
from django.http import HttpResponse
from .models import SubmitJob, ApplyJob

# Create your views here.

#home page

def index (request):
    template = "index.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Job Board',
    }
    return render(request, template,context)

#job page
def jobs (request):
    template = "jobs.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#candidate page
def candidate (request):
    template = "candidate.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#job details page
def job_details (request):
    template = "job_details.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#elements page
def elements (request):
    template = "elements.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#blog page
def blog (request):
    template = "blog.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#single-blog page
def single_blog (request):
    template = "single-blog.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#contact page
def contact (request):
    template = "contact.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

#job_vacant
def detail(request, job_id):
    template = "job_detail_{{job_id}}.html"
    jobs = SubmitJob.objects.get(pk=job_id)
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)    