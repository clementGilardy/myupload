from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    name = models.CharField(max_length=100)
    autor = models.ForeignKey(User)
    path = models.CharField(max_length=300)
    size = models.IntegerField()
    format = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
