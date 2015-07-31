from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    path = models.CharField(max_length=300)
    size = models.IntegerField(null=True)
    icon = models.CharField(max_length=300,null=True)
    format = models.CharField(max_length=10,null=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
