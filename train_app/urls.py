from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'main_name'),
    path('register/', views.RegisterUser.as_view(), name = 'register_user_name'),
    path('login/', views.LoginUser.as_view(), name = 'login_user_name'),
    path("user_page/", views.UserPage.as_view(), name="user_page_name"),
    path("logout/", views.logout_view, name="logout_name")
]