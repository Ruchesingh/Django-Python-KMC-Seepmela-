from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from home.forms import StudentForm
from home.models import Student

# Create your views here.
def home(request):
    print("Home from django !!")
    return HttpResponse("<b> Hello from django </b>")

def home_json(request):
    data={
        "name":"Ruchee",
        "address":"Mnr"
    }
    return JsonResponse(data)


def landing_page(request):
    user_info ={
        "name":"Ruchee Singh"
    }
    return render(request,'home/index.html',user_info)

def student_list(request):
    student=Student.objects.all() # list ma 
    context = {
        "student":student
    }
    return render(request,'student/index.html', context)


def student_create(request):
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        Student.objects.create(
            name = data['student_name'],
            number = data['number'],
            dob = data['dob']
        )
        return redirect('/home/student_list')

    return render(request, 'student/student_create.html')

def student_create2(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'student/student_create2.html', context)


def student_update(request,id):
    print("this is id from url", id)
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/home/student_list')
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, 'student/student_update.html', context)


def student_delete(request,id):
    student = Student.objects.filter(id=id).delete()
    return redirect('/home/student_list')
    
