from django.db import models
from django.db.models import Model


# Create your models here.

class SubmitJob(models.Model):
    company_name = models.CharField(default='', max_length=255)
    company_img = models.ImageField('Company Image', default='')
    job_vacancy = models.CharField(default='', max_length=255)
    job_category = models.CharField(default='', max_length=255)
    pub_date = models.DateTimeField('date published', auto_now_add=False, blank=True)
    job_description = models.CharField('Job Description',default='', max_length=255)
    salary = models.IntegerField(default=0)
    location = models.CharField('Location',default='',max_length=255)
    time_employment = models.CharField(default='',max_length=200)
    
    
    def __str__(self) -> str:
        return self.company_name

class ApplyJob(models.Model):
    job = models.ForeignKey(SubmitJob, on_delete=models.CASCADE)
    employee_name = models.CharField('Name', default='', max_length=255)
    employee_email = models.EmailField('Email', default='', max_length=255)
    employee_website = models.CharField('Website/link', default='', max_length=255)
    employee_cv = models.FileField('Upload your CV here')
    employee_coverletter = models.CharField('Coverletter', default='', max_length=255)

    def __str__(self) -> str:
        return self.employee_name