from app.models import Customer, PostHome, PostAbout, PostService, PostVision
from rest_framework import serializers



class CustomerSerializer(serializers.ModelSerializer):
 class Meta:
  model = Customer
  fields = ['name','email','target','address','city','zipcode','state','message']


class HomeSerializer(serializers.ModelSerializer):
 class Meta:
  model = PostHome
  fields = ['banner_homeImage1','banner_homeImage2','banner_homeImage3','banner_review_image1','banner_review_image2','banner_review_image3']

class AboutSerializer(serializers.ModelSerializer):
 class Meta:
  model = PostAbout
  fields = ['banner_Abtimage1','banner_Abtimage2','banner_Abtimage3','aboutheading','banner_carAboutImage1','banner_carAboutImage2','banner_carAboutImage3','banner_carAboutImage4','banner_carAboutImage5','Aboutbody']


class VisionSerializer(serializers.ModelSerializer):
 class Meta:
  model = PostVision
  fields = ['banner_Visimage1','banner_Visimage2','banner_Visimage3','Vision_heading', 'Visionbody']


class ServiceSerializer(serializers.ModelSerializer):
 class Meta:
  model = PostService
  fields = ['Service_heading','banner_serv1','banner_serv2','banner_serv3','Servicebody']