import django
from django.shortcuts import get_object_or_404, redirect, render    

from movie.forms import CategoryForm, MovieForm
from movie.models import Category, Movie

# Create your views here.
# display all the list of category
def category_list(request):
    data = Category.objects.all()
    context = {
        "category":data
    }
    return render(request, 'category/index.html', context)

# create a new category
def category_create(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')   # use URL name
        else:
            print(form.errors)   # IMPORTANT

    return render(request, 'category/create.html', {
        'form': form
    })

# display all the list of movie
def movie_list(request):
    data = Movie.objects.all()
    context = {
        "movie":data
    }
    return render(request, 'movie/index.html', context)

# create a new movie

def movie_create(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('movie_list')   # use URL name
        else:
            print(form.errors)   # IMPORTANT

    return render(request, 'movie/create.html', {
        'form': form
    })
    

    

