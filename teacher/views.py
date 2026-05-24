# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect

import teacher
from teacher.form import GradeForm, TeacherForm
from teacher.models import Grade, Teacher

#Teacher...

def teacher_list(request):
    data = Teacher.objects.all()
    context = {
        "teacher":data
    }
    return render(request, 'teacher/index.html', context)

def teacher_create(request):
    teacher_form = TeacherForm()
    if request.method == "POST":
        teacher_form = TeacherForm(data=request.POST)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('/grade/teacher')
    context = {
        "form":teacher_form
    }
    return render(request,'teacher/teacher_create.html', context)
def teacher_update(request, id):

    form = TeacherForm(instance=teacher)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect('teacher_list')

    context = {
        'form': form
    }
    return render(request, 'teacher/teacher_update.html', context)

def teacher_delete(request, id):
    teacher = Teacher.objects.filter(id=id).delete()
    return redirect('/teacher/teacher_list')

# Grade...

def grade_list(request):
    grades = Grade.objects.all()
    context = {
        'grades': grades
    }
    return render(request, 'grade/index.html', context)

def grade_create(request):
    form = GradeForm()

    if request.method == "POST":
        form = GradeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('grade_list')

    context = {
        'form': form
    }
    return render(request, 'grade/grade_create.html', context)

def grade_update(request, id):

    form = GradeForm(instance=Grade)

    if request.method == "POST":
        form = GradeForm(request.POST, instance=Grade)

        if form.is_valid():
            form.save()
            return redirect('grade_list')
        
def grade_delete(request, id):
    grade = Grade.objects.filter(id=id).delete()
    return redirect('/grade/grade_list')        