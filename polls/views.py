from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import info
# Create your views here.

def message(request,forid):
    # try:
    #     some=info.objects.get(id=forid)
    #     return HttpResponse('hello world')
    # except:
    #     return HttpResponse('wrong')
    some=get_object_or_404(info,id=forid)
    return HttpResponse('aaa')