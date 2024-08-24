from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Education(models.Model):
    degree = models.CharField(max_length=4, default="B.A.")
    field_of_study = models.CharField(max_length=70, default="History")   
    school = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=2, default="MD")

class Experience(models.Model):
    position = models.CharField(max_length=100)
    year_begin = models.DateField()
    year_end = models.DateField()
    description = models.TextField(max_length=1050)
    
class Resume(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    brand_statement = models.TextField(max_length=1050)
    education = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
