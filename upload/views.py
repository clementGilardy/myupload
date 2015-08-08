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
@csrf_exempt
def documents (request,id=None):
    folder = Document.objects.get(id=id)
    if folder != None:
        documents = Document.objects.filter(docContains=folder.id).exclude(id=folder.id)

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

    json_data = json.dumps({"response":False})
    if os.path.exists(directoryUser):
        iconFile = os.path.join('/static','upload','images','closed_folder.png')
        if parent != None and parent != "":
            docParent = Document.objects.get(id=parent)
            realPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'documents',docParent.path,nameOfFolder)
            if os.path.exists(realPath) == False:
                document = Document(name=nameOfFolder,author=request.user,docContains=docParent,path=os.path.join(docParent.path,nameOfFolder),realPath=realPath,icon=iconFile,format="folder")
                document.save()
                os.mkdir(realPath)
                json_data = json.dumps({"response":True,'name':document.name,'id':document.id,'icon':document.icon})

    return HttpResponse(json_data, content_type="application/json")

