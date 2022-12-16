from django.db import models

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Subskill(models.Model):
    title = models.CharField(max_length=40)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    company = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.fname + ' ' + self.lname