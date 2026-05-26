from django.urls import path

from teacher.views import TeacherCreate, TeacherUpdate, grade_create, grade_delete, grade_list, grade_update, teacher_create, teacher_delete, teacher_list, teacher_update, TeacherView
TeacherCreate, TeacherUpdate
urlpatterns=[
    # grade
    path('grade/', grade_list, name='grade'),
    path('grade_create/', grade_create, name='gcreate'),
    path('grade_update/<int:id>/', grade_update, name='gupdate'),
    path('grade_delete/<int:id>/', grade_delete, name='gdelete'),
    path('teacher-class-list',TeacherView.as_view(), name="teacher-class"),
    path('teacher-class-create',TeacherCreate.as_view(), name="teacher-class-create"),
    path('teacher-class-update/<int:pk>',TeacherUpdate.as_view(), name="teacher-class-update"),

    # teacher
    path('teacher/',teacher_list, name="teacher"),
    path('teacher_create/', teacher_create, name='tcreate'),
    path('teacher_update/<int:id>/', teacher_update, name='tupdate'),
    path('teacher_delete/<int:id>/', teacher_delete, name='tdelete'),
]
  
