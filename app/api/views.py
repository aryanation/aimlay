from app.models import Customer, PostHome, PostAbout, PostService, PostVision
from app.api.serializers import CustomerSerializer, HomeSerializer, AboutSerializer, ServiceSerializer, VisionSerializer
from rest_framework import viewsets
from rest_framework.views import APIView

class CustomerView(viewsets.ModelViewSet):
 queryset = Customer.objects.all()
 serializer_class = CustomerSerializer

class AboutView(viewsets.ModelViewSet):
 queryset = PostAbout.objects.all()
 serializer_class = AboutSerializer


class HomeView(viewsets.ModelViewSet):
 queryset = PostHome.objects.all()
 serializer_class = HomeSerializer


class ServiceView(viewsets.ModelViewSet):
 queryset = PostService.objects.all()
 serializer_class = ServiceSerializer


class VisionView(viewsets.ModelViewSet):
 queryset = PostVision.objects.all()
 serializer_class = VisionSerializer
