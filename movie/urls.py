
from django.urls import path

from movie.views import category_create, category_list, movie_create, movie_list

urlpatterns=[
    
        path('category_list/', category_list, name='category_list'),
        path('category_create/', category_create, name='category_create'),
        path('movie_list/', movie_list, name='movie_list'),
        path('movie_create/', movie_create, name='movie_create'),
]