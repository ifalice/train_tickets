from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'main_name'),
    path('register/', views.RegisterUser.as_view(), name = 'register_user_name')
]