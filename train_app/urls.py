from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name = 'main_name'),
    path('register/', views.RegisterUser.as_view(), name = 'register_user_name'),
    path('login/', views.LoginUser.as_view(), name = 'login_user_name'),
    path("user_page/", views.UserPage.as_view(), name="user_page_name"),
    path("logout/", views.logout_view, name="logout_name"),
    path('get_data_train_car/', views.BuyTicket.get_data_train_car, name = 'data_train_car_name'),
    path('buy_ticket/', views.BuyTicket.as_view(), name = 'buy_ticket_name'),
    path('buy_ticket/order_ticket/', views.OrderTicketView.as_view(), name = 'order_ticket_name'),
    path('buy_ticket/get_true_seats/', views.get_true_seats, name = 'get_true_seats_name'),
    
]
    