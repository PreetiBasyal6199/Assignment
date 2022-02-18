from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import New_Data
import csv
import os,io
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def LoginView(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form =AuthenticationForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' wecome {username} !!')
            return render(request,'import_data/home.html')
        else:
            print("error")
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'import_data/login.html', {'form':form, 'title':'log in'})
@csrf_exempt
@login_required
def import_data(request):
     
     if request.method=="POST":
         file=request.FILES['importData']
         if not file.name.endswith('.csv'):
             print('This is not csv file')
         data_set=file.read().decode('UTF_8')
         io_string=io.StringIO(data_set)
         next (io_string)
         
         for column in csv.reader(io_string,delimiter=','):
                if column!=[]:
                  current_user=User.objects.get(id=request.user.id)
                  name=current_user.username
                  new_data=New_Data.objects.create(full_name=column[0],date_of_birth=column[1],gender=column[2],salary=column[3],designation=column[4],imported_by=name)
                  new_data.save() 
                  datas=New_Data.objects.all()
                else:
                    print  ("The field is empty")
           
                 
         return render(request,'import_data/list.html',{'datas':datas})



def SearchView(request):
     item=request.GET.get("catagory")
     datas=New_Data.objects.filter(username=item)| New_Data.objects.filter(imported_at__icontains=item)
     return render(request,'import_data/search.html',{'obj':datas})