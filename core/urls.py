from django.contrib import admin
from django.urls import path,include

from .views import (home_page,
                    register,
                    logout_request,
                    login_request,
                     list_exercises,
                      exercise,
                      add_exercise,
                      add_category,saveans)
app_name = 'main'
urlpatterns = [
    path('', home_page),
    path('register/', register),
    path('login/', login_request),
    path('logout/', logout_request),
    path('add-exercise/', add_exercise),
    path('add-category/', add_category),
    path('saveans/', saveans),



    path('<id>/exercise/', exercise),
    path('list-exercises/', list_exercises),
 


]
