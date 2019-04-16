from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	# path('', auth_views.LoginView.as_view(template_name='Login/login.html'), name='login'),
	path('', views.logging, name='login'),
	path('register/', views.registering, name='register'),
	path('execute/', views.execute_query, name='execute'),
	path('evaluate/', views.evaluate, name='evaluate'),
	path('resume/', views.upload, name='resume'),
	path('chatbot/', views.call_chatbot, name='chatbot'),
	path('main/', views.call_main, name='main'),
	path('placement/', views.place, name='placement'),
]