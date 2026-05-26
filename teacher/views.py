from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required



# Create your views here.
# display all the list of teacher
@login_required()
def teacher_list(request):
    data = Teacher.objects.all()
    context = {
        "teacher":data
    }
    return render(request, 'teacher/index.html', context)

# create a new teacher
@login_required(login_url='/user/login')
def teacher_create(request):
    form = TeacherForm()

    if request.method == "POST":
        form = TeacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('teacher')   # use URL name
        else:
            print(form.errors)   # IMPORTANT

    return render(request, 'teacher/teacher_create.html', {
        'form': form
    })

# update the data of teacher
def teacher_update(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(instance=teacher)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return redirect('teacher')
        else:
            print(form.errors)

    return render(request, 'teacher/teacher_update.html', {
        'form': form
    })

# delete the teacher from the list
def teacher_delete(request, id):
    teacher = Teacher.objects.filter(id=id).delete()
    return redirect('teacher')


from teacher.form import TeacherForm
from teacher.form import GradeForm
from teacher.models import Grade, Teacher


def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade/index.html', {
        'grades': grades
    })


def grade_create(request):
    form = GradeForm()

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade')

    return render(request, 'grade/grade_create.html', {
        'form': form
    })


def grade_update(request, id):
    grade = Grade.objects.get(id=id)
    form = GradeForm(instance=grade)

    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade')

    return render(request, 'grade/grade_update.html', {
        'form': form
    })


def grade_delete(request, id):
    grade = Grade.objects.get(id=id)
    grade.delete()
    return redirect('grade')