from datetime import date
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from admissions.models import Admission
from .forms import Admission_form

# Create your views here.



"""Belwo function written for add and show data"""
@csrf_exempt
def home(request):
    if request.method == 'POST':
        # print('Data is valid')

        data=Admission_form(request.POST)
        # file = Admission_form(request.FILES)
        if data.is_valid():
            print('Data is valid')
            nm=data.cleaned_data['name']
            cs=data.cleaned_data['course']
            mail=data.cleaned_data['email']
            mob=data.cleaned_data['mobile']
            file = data.cleaned_data['identification_photo']
            dt=date.today()
            Admission.objects.create(name=nm,course=cs,email=mail,mobile=mob,admission_date=dt,identification_photo=file)
            return redirect('homepage')
        else:
            print("Data is invalid")
            return HttpResponse("Invalid data entered")
    else:
        form=Admission_form()
    stud= Admission.objects.all()
    return render(request,template_name='admission.html',context={'form':form,'stud':stud})
    
"""Below function is written for delete the data"""
def delete_stud(request,id):
    Admission.objects.get(id=id).delete()
    return redirect('homepage')


"""Below function is written for edit the data"""
@csrf_exempt
def edit_stud(request,id):
    if request.method == 'POST':
        stud_obj=Admission.objects.get(id=id)
        stud_mod=Admission_form(request.POST,instance=stud_obj)
        if stud_mod.is_valid():
            stud_mod.save()
    else:
        stud_obj=Admission.objects.get(id=id)
        stud_mod=Admission_form(instance=stud_obj)
    return render(request,template_name='update.html',context={'stud':stud_mod})