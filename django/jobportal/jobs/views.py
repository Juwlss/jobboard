from django.shortcuts import render
from django.http import HttpResponse
from .models import SubmitJob, ApplyJob

# Create your views here.


def index (request):
    template = "index.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'title': 'Find a Job',
    }
    return render(request, template,context)

def detail(request, job_id):
    return HttpResponse(f"You are looking for job {job_id}")