from django.shortcuts import render
import os
from upload.models import Document
from django.shortcuts import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import pickle, pprint

def home (request):
    return render(request, 'index.html')

@login_required
def documents (request):
    return render(request, 'document.html',locals())

@csrf_exempt
def add_folder(request):
    post= request.POST['name_folder']
    nameOfFolder = json.loads(post)
    directoryUser = os.path.join(os.path.dirname(os.path.abspath(__file__)),'documents',request.user.username, nameOfFolder) 
    if os.path.exists(directoryUser) == False:
        os.mkdir(directoryUser)
        if os.path.exists(directoryUser):
            iconFile = os.path.join('/static','upload','images','closed_folder.png')
            document = Document(name=nameOfFolder,author=request.user,path=request.user.username+'/'+nameOfFolder,realPath=directoryUser,icon=iconFile,format="folder")
            document.save()
        json_data = json.dumps({"HTTPRESPONSE":True})
    else:
        json_data = json.dumps({"HTTPRESPONSE":False})

    return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def display_folder(request):
    id = json.loads(request.POST['id_doc'])
    directoryUser = os.path.dirname(os.path.abspath(__file__)) + '/documents/' + request.user.username 
    if os.path.exists(directoryUser) == False:
        os.mkdir(directoryUser)

    listFileUser = []
    fileContains = []
    if id == None or id == "" :
        fileUser = Document.objects.filter(author=request.user)

        for folder in fileUser:
            listFileUser.append([folder.name,folder.format,folder.icon,os.path.join(directoryUser,folder.name),folder.id])
        json_data = json.dumps({'fileUser':listFileUser})
    else: 
        fileUser = Document.objects.filter(id=id)
        if fileUser != None:
            for folder in fileUser:
                listFileUser.append([folder.name,folder.format,folder.icon,os.path.join(directoryUser,folder.name)])
                if folder.docContains != None:
                    doc = Document.objects.filter(id=folder.docContains)
                    fileContains.append([doc.name,doc.format,doc.icon,os.path.join(directoryUser,doc.name)])
            json_data = json.dumps({'fileUser':fileContains})



    return HttpResponse(json_data,content_type="application/json")
