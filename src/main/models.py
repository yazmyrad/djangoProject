from django.db import models
from register.models import Profile
from study.models import Blog

class Interaction(models.Model):
    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE)
    relate = models.CharField(max_length=5, choices={"LKE":"Like", "SVE":"Save", "SHR":"Share"})
    timestamp = models.TimeField()