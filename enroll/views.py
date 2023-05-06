from django.shortcuts import render
from . forms import sigupform
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm=sigupform(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully !!!')
            fm.save()
    else:
     fm=sigupform()
    return render(request,'enroll/signup.html',{'form':fm})

