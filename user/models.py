from django.db import models
from django.contrib.auth.models import User
from upload.models import Document

class Profil(models.Model):
    user = models.OneToOneField(User)
    mainDocument = models.OneToOneField(Document)
    
    
