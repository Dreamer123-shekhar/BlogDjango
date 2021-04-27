'''from django.shortcuts import render'''
from django.shortcuts import render
from .models import Name #. means we are in same directory
from .models import Email
def index(req):
    return render(req,'index.html')


def newPage(request):
  na  =request.POST.get('name1')

  o_ref = Name(name=na)
  o_ref.save()


  return render(request,'index.html',{"message": "Registered for Shekhar BBQ"})




'''# Create your views here.

def index(request):
    return HttpResponse('Hello this is Shekhar')

def index2(response):
    return HttpResponse("I am the second landing page")

def index3(response):
    return HttpResponse("I am the last page on your user interface")'''

