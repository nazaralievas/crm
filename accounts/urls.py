from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('user/', userPage, name='user'),
    path('account/', accountSettings, name='account'),

    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),

    path('create_order/<str:pk>/', createOrder, name='create_order'),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),
]
