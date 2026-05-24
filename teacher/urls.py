
from django.urls import path

from teacher.views import grade_create, grade_delete, grade_list, grade_update, teacher_create, teacher_delete, teacher_list, teacher_update

urlpatterns=[
    path('teacher',teacher_list, name="teacher"),
    path('teacher_create',teacher_create, name="teacher-create"),
     path('teacher_update/<int:id>', teacher_update, name="teacher_update"),
    path('teacher_delete/<int:id>', teacher_delete, name="teacher_delete"),
    
    
     path('grade/',grade_list, name="grade_list"),
    path('grade-create/',grade_create, name="grade_create"),
    path('grade-update/<int:id>/',grade_update, name="grade_update"),
    path('grade-delete/<int:id>/',grade_delete, name="grade_delete"),
]
    
  
