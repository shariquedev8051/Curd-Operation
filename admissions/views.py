from admissions.models import Admission
from django import forms
from django.shortcuts import redirect, render
from .forms import Admission_form
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from datetime import date
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        data=Admission_form(request.POST)
        if data.is_valid():
            print('Data is valid')
            nm=data.cleaned_data['name']
            cs=data.cleaned_data['course']
            mail=data.cleaned_data['email']
            mob=data.cleaned_data['mobile']
            dt=date.today()
            Admission.objects.create(name=nm,course=cs,email=mail,mobile=mob,admission_date=dt)
            return redirect('homepage')
        else:
            print("Data is invalid")
        # stud_obj=Admission(data)
        # stud_obj.save()
        # print(Admission.objects.all())
    else:
        form=Admission_form()
        return render(request,template_name='admission.html',context={'form':form})
    
    