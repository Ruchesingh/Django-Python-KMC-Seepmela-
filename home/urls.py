
from django.urls import path
from home.views import home, home_json, landing_page, student_create, student_delete, student_list,student_create2, student_update


urlpatterns=[
    path('home/',home,name="home"), # reference naming last one 'name wala' but browser ma agadi kai chaiyenxaa
    path('json/',home_json, name="json_data"),
    path('home_page',landing_page, name="page"),
    path('student_list', student_list,name="student"),
    path('student_create', student_create,name="student"),
    path('student_create2', student_create2,name="create2"),
     path('student_update/<int:id>', student_update, name="update"),
     path('student_delete/<int:id>', student_delete, name="delete"), 
    
]