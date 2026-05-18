from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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