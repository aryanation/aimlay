from django.urls import path, include
from app.api import views
from rest_framework import routers




# creating router object
router = routers.DefaultRouter()

#register router
router.register('homes', views.HomeView, basename='homes')
router.register('custom', views.CustomerView, basename='custom')
router.register('abouts', views.AboutView, basename='abouts')
router.register('visions', views.VisionView, basename='visions')
router.register('serivces', views.ServiceView, basename='services')


urlpatterns = [
    path('api/', include(router.urls)),
]