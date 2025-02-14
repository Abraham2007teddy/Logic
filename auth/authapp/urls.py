from django.urls import path
from . import views

urlpatterns = [
    path('check-user/', views.check_user_exists, name='check_user_exists'),
    path('create-user/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
