from django.shortcuts import render,redirect
from .models import Profile
from django.contrib import messages

# Create your views here.
def index(request):
    profile_objects = Profile.objects.all()

    return render(request, 'pdf_generator/index.html',{'profile_objects':profile_objects}) 

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        scills = request.POST.get("scills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,scills=scills)
        profile.save()
        messages.success(request,'Thank you. You information is accepted')
        return redirect('index')

    return render(request, 'pdf_generator/accept.html') 

def resume(request,id):
    user_profile = Profile.objects.get(id=id)

    return render(request, 'pdf_generator/resume.html',{'user_profile':user_profile})
