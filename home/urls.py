
from django.urls import path
from home.views import home, home_json, landing_page


urlpatterns=[
    path('home/',home,name="home"), # reference naming last one 'name wala' but browser ma agadi kai chaiyenxaa
    path('json/',home_json, name="json_data"),
    path('home_page',landing_page, name="page")
]