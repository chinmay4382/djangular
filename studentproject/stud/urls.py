from django.urls import path
from . import views


urlpatterns = [
    path('', views.Student_list),
    path('<int:pk>/', views.Student_detail),
]
