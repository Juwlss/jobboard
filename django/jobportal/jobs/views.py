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
        'available' : len(jobs),
        'title': 'Job Board',
    }
    return render(request, template,context)

#job page
def jobs (request):
    template = "jobs.html"
    jobs = SubmitJob.objects.all()
    context = {
        'jobs': jobs,
        'available' : len(jobs),
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
def job_details(request, job_id):
    template = "job_details.html"
    jobs = SubmitJob.objects.get(pk=job_id)
    context = {
        'jobs': jobs,
        'title': 'Job Details',
    }
    if request.method == 'POST':
            job_id = jobs.id
            employee_name = request.POST.get("employee_name")
            employee_email = request.POST.get("employee_email")
            employee_website = request.POST.get("employee_website")
            employee_coverletter = request.POST.get("employee_coverletter")
            employee_cv = request.POST.get("employee_cv")
            
            ApplyJob.objects.create(job_id = jobs.id, employee_name=employee_name, employee_email=employee_email, employee_website=employee_website, 
                                    employee_coverletter=employee_coverletter, employee_cv=employee_cv)
            
            
            
            print(employee_name, employee_email, employee_website, employee_coverletter, employee_cv)
    return render(request, template,context)

# def apply_job(request, job_id):
#     template = "job_details.html"
#     jobs = SubmitJob.objects.get(pk=job_id)
#     context = {
#             'jobs': jobs,
#             'title': 'Job Details',
#     }   
    


# #job details page
# def job_apply(request, job_id):
#     template = "jobs.html"
#     jobs = SubmitJob.objects.all()
#     context = {
#         'jobs': jobs,
#         'title': 'Job Details',
#     }
#     return render(request, template,context) 

# #job details page
# def detail (request, job_id):
#     template = "job_details.html"
#     jobs = SubmitJob.objects.get(pk=job_id)
#     context = {
#         'jobs': jobs,
#         'title': 'Find a Job',
#     }
#     return render(request, template,context)

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

   