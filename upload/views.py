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
    post = request.POST['name_folder']
    nameOfFolder = json.loads(post)
    id_parent = request.POST.get('id_parent',False)
    if id_parent != False:
        parent  = json.loads(id_parent)
    else:
        parent = None
    
    directoryUser = os.path.join(os.path.dirname(os.path.abspath(__file__)),'documents',request.user.username) 

    if os.path.exists(directoryUser):
        iconFile = os.path.join('/static','upload','images','closed_folder.png')
        if parent != None and parent != "":
            docParent = Document.objects.get(id=parent)
            realPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'documents',docParent.path,nameOfFolder)
            document = Document(name=nameOfFolder,author=request.user,docContains=docParent,path=os.path.join(docParent.path,nameOfFolder),realPath=realPath,icon=iconFile,format="folder")
            document.save()
        else:
            docUser = Document.objects.get(author=request.user,path=request.user.username)
            realPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'documents',request.user.username,nameOfFolder)
            document = Document(name=nameOfFolder,author=request.user,docContains=docUser,path=request.user.username+'/'+nameOfFolder,realPath=os.path.join(directoryUser,nameOfFolder),icon=iconFile,format="folder")
            docParent = Document.objects.get(path=request.user.username)
            document.save()

        os.mkdir(realPath)
        json_data = json.dumps({"HTTPRESPONSE":True})
    else:
        json_data = json.dumps({"HTTPRESPONSE":False})

    return HttpResponse(json_data, content_type="application/json")

@csrf_exempt
def display_folder(request):
    print(request.POST['id_doc'])
    id = json.loads(request.POST['id_doc'])
    directoryUser = os.path.dirname(os.path.abspath(__file__)) + '/documents/' + request.user.username 
    iconFile = os.path.join('/static','upload','images','closed_folder.png')

    if os.path.exists(directoryUser) == False:
        docUser = Document(name=request.user.username,author=request.user,path=request.user.username,realPath=directoryUser,icon=iconFile,format="folder")
        docUser.save()
        os.mkdir(directoryUser)

    listFileUser = []
    fileContains = []
    if id == None or id == "" :
        docUser = Document.objects.get(author=request.user,path=request.user.username)
        fileUser = Document.objects.filter(docContains=docUser.id)

        for folder in fileUser:
            listFileUser.append([folder.name,folder.format,folder.icon,os.path.join(directoryUser,folder.name),folder.id,folder.path])
        json_data = json.dumps({'fileUser':listFileUser})
    else: 
        folder = Document.objects.get(id=id)
        if folder != None:
            fileUser = Document.objects.filter(docContains=folder.id)
            for file in fileUser:
                fileContains.append([file.name,file.format,file.icon,os.path.join(directoryUser,file.name),file.id,file.path])
        json_data = json.dumps({'fileUser':fileContains})

    return HttpResponse(json_data,content_type="application/json")
