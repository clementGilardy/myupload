from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required
from upload.models import Document
from user.models import Profil
import os

def connexion(request):
    error = False

    if request.method == "POST":
        form = forms.ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = forms.ConnexionForm()
    return render(request,'connexion.html',locals())

@login_required
def deconnexion(request):
    logout(request)
    return redirect('/upload/accueil')

def inscription(request):
    inscription = None
    if request.method == "POST":
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = forms.models.User.objects.create_user(username,email,password)
            directoryUser = "/srv/http/myupload/upload/documents/"+username
            document = Document(name=username,author=user,path=username,realPath=directoryUser,format="folder")
            document.save()
            profil = Profil(user=user,mainDocument=document)
            profil.save()
            inscription = True
            if os.path.exists(directoryUser) == False:
                os.mkdir(directoryUser)
            return render(request,'index.html',locals())
    form = forms.InscriptionForm()
    return render(request,'inscription.html',locals()) 
