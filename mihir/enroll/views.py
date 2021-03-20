from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def myfrom(request):
    if(request.method=="POST"):
        fm=UserCreationForm(request.POST)
        if(fm.is_valid()):
            fm.save()
            fm=UserCreationForm()
    else:
        fm=UserCreationForm()
    return render(request,"enroll/base.html",{"form":fm})
