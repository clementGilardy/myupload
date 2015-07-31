from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required

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
    error = False

    if request.method == "POST":
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            user = forms.models.User.objects.create_user(username,email,password)
            user.save()
    else:
        form = forms.InscriptionForm()

    return render(request,'inscription.html',locals()) 
