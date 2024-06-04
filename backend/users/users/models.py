from django.db import models


class Occupations(models.Model):
    job_title = models.CharField(max_length=50, primary_key = True)
    job_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.job_title + " - " + self.job_description

class Users(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=25)
    email = models.EmailField(max_length=50)
    job_title = models.ForeignKey(Occupations, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.job_title

