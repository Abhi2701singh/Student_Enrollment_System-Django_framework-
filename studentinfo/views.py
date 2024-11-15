                                     
from django.shortcuts import render
from .forms import studForm 
from .forms import SForm
from .models import stud

# Create your views here.
def show(request):
    return render(request, "home.html")

def register(request):
    title = "New Student Registration"
    form = studForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['s_name']
        course = form.cleaned_data['s_course']
        branch = form.cleaned_data['s_branch']
        roll = form.cleaned_data['s_roll']
        college = form.cleaned_data['s_college']
        email = form.cleaned_data['s_email']

        if stud.objects.filter(s_roll=roll).exists():
            # Display an error message to the user if roll number exists
            context = {
                "title": title,
                "form": form,
                "error_message": "Roll number already exists. Please use a unique roll number."
            }
            return render(request, 'register.html', context)

        p = stud(s_name=name,s_course=course,s_branch=branch,s_roll=roll,s_college=college,s_email=email)
        p.save()
        return render(request, 'ack.html', {"title":"Registered Successfully"})


    context = {
        "title": title,
        "form": form,
    }
    return render(request, 'register.html', context)

def existing(request):
    title = "All Registered Student"
    queryset = stud.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existing.html',context)

def search(request):
    title = "Search Student"
    form = SForm(request.POST or None)
    if form.is_valid():
        roll = form.cleaned_data['s_roll']
        queryset = stud.objects.filter(s_roll =roll)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Student Details Not Found'})
        context ={
            'title':title,
            'queryset':queryset,
        }
        return render(request,'existing.html',context)
    context ={
        'title':title,
        'form':form,
    }
    return render(request,'search.html',context)

def dropout(request):
    title = "Drop Out"
    form = SForm(request.POST or None)
    if form.is_valid():
        roll = form.cleaned_data['s_roll']
        queryset = stud.objects.filter(s_roll =roll)
        if len(queryset)==0:
            return render(request,'ack.html',{'title':'Student Details Not Found'})
        else:
            queryset = stud.objects.filter(s_roll =roll).delete()
            return render(request,'ack.html',{'title':"Student removed from your database"})
    context ={
        'title':title,
        'form':form,
    }
    return render(request,'search.html',context)

