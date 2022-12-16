from django.urls import path
from LoginApp import views

urlpatterns = [
    path('login/', views.login_view),
]