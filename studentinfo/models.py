from django.db import models

# Create your models here.
class stud(models.Model):
    s_name  = models.CharField(max_length=30)
    s_course  = models.CharField(max_length=30)
    s_branch = models.CharField(max_length=30)
    s_roll = models.IntegerField(null=True, blank=True)
    s_college  = models.CharField(max_length=30)
    s_email = models.EmailField(max_length=30)