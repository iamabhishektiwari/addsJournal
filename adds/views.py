# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Advertisment
from forms import DocumentForm


def home(request):
  documents = Advertisment.objects.all()
  return render(request, "index.html",{'documents':documents})


def pp(request):
  return render(request, "alert_post.html")


def list(request):
    
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Advertisment(docfile = request.FILES['docfile'],
                                  Add_title = request.POST['Add_title'],
                                  Add_brand = request.POST['Add_brand'],
                                  Add_about = request.POST['Add_about'],
                                  Add_entry_dt = request.POST['Add_entry_dt'],)
            newdoc.save()
            
            # Redirect to the document list after POST
            return HttpResponseRedirect('/adds/list/')
    else:
        form = DocumentForm() # A empty, unbound form


    # Load documents for the list page
    documents = Advertisment.objects.all()

    # Render list page with the documents and the form

    
    return render(request, "list.html",{'documents':documents,'form':form})

    





####for file field

# def list(request):
    
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect('/adds/list/')
#     else:
#         form = DocumentForm() # A empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form

    
#     return render(request, "list.html",{'documents':documents,'form':form})


# def index(request):
#     return render_to_response('myapp/index.html')