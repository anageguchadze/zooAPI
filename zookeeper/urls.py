from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategotyDetail.as_view()),
    path('animals/', AnimalList.as_view()),
    path('animals/<int:pk>/', AnimalDetail.as_view()),
]