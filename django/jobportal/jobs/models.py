from django.db import models

# Create your models here.

class SubmitJob(models.Model):
    company_name = models.CharField(max_length=255)
    job_vacancy = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    job_description = models.CharField(max_length=255)
    salary = models.IntegerField('salary')
    location = models.CharField(max_length=255)
    time_employment = models.CharField(max)
    

class ApplyJob(models.Model):
     employee_name = models.CharField(max_length=255)
     employee_email = models.EmailField(max_length=255)
     employee_website = models.EmailField(max_length=255)
     employee_cv = models.FileField
     employee_coverletter = models.CharField(max_length=255)
