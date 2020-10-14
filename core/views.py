from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm,SolveExercise,AddExercise,AddCategory
from .models import Exercise,Category, Profile
from django import forms
from django.core.paginator import Paginator
import json

# Create your views here.
def home_page(request):
    return render(request, 'core/home.html')

def register(request):
    
    if request.method == 'POST':
        form= NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")

    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'core/register.html',context)
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect("/")
    form = AuthenticationForm()
    context = {
        "form":form
    }
    return render(request, 'core/login.html',context)
def logout_request(request):
    logout(request)
    return redirect("/")

def list_exercises(request):
    categories = Category.objects.all()
    
    if request.user.is_authenticated:
        context = {
        "categories":categories
    }   
        return render(request, 'core/list_exercises.html',context)
    else:
        return redirect("main:login_request")

        


def exercise(request,id):
    category = Category.objects.get(id=id)
    exercises = category.exercise_set.all()
    p = Paginator(exercises,1)
    try:

        page_number = request.GET.get('page',1)
    except:
        page_number = 1 
    try:
        exercise = p.get_page(page_number)
    except (EmptyPage,InvalidPage):
            page_number = p.page(p.num_pages)

    context = {
        "exercises":exercises,
        "exercise":exercise
    }

   
       
       
    return render(request,"core/exercise.html",context)

def add_exercise(request):
    if request.method == 'POST':
        form = AddExercise(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.author = request.user
            exercise.save()
    form = AddExercise()
    return render(request,"core/add_exercise.html",{'form':form})


def add_category(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            category = form.save()
            category.slug = form.cleaned_data.get("name").lower()
    form = AddCategory()
    return render(request,"core/add_category.html",{'form':form})

def saveans(request):
    ans = request.GET['ans']
    exercise_id = request.GET['question']
    exercise = Exercise.objects.get(id=exercise_id)
    profile = Profile.objects.get(user = request.user.id)  
    
    if(ans==exercise.correct):
          profile.points +=1
          profile.save()    
          print(profile.points)

    else:
        print("Incorrect")

    print(exercise_id)
    print(ans)
    return HttpResponse("bravo")
    