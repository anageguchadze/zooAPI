from django.urls import path, include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategotyDetail.as_view()),
    path('animals/', AnimalList.as_view()),
    path('animals/<int:pk>/', AnimalDetail.as_view()),
    # path('animals/batch-delete/', AnimalBatchDeleteView.as_view()),
]