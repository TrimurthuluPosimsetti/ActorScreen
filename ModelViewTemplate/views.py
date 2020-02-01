# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def ScreenTime(request):
    if(request.method=="POST"):
        Sform=ScreenTimeForm(request.POST,request.FILES)
        videofile=request.GET['files']
        return HttpResponse("GOt it")
    else:    
        Sform=ScreenTimeForm()
        return render(request,'index.html',{'form':Sform})
