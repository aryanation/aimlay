from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('ref/', views.referral.as_view(), name='ref'),
    path('student/', views.student.as_view(), name='student'),
    path('business/', views.business.as_view(), name='business'),
    path('about/', views.about.as_view(), name='about'),
    path('vision/', views.vision, name='vision'),
    path('services/', views.services, name='service'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('join/', views.join, name='join'),
    path('form/', views.Query.as_view(), name='form'),
]
