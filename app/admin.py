from django.contrib import admin
from . import models
from .models import Customer, PostHome, PostAbout, PostService, PostVision, Student, Business, Refferal, quickuser

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
 list_display = ['name','email','target','address','city','zipcode','state','message']


@admin.register(PostHome)
class HomeAdmin(admin.ModelAdmin):
 list_display = ['banner_homeImage1','banner_homeImage2','banner_homeImage3','banner_review_image1','banner_review_image2','banner_review_image3']


@admin.register(PostAbout)
class AboutAdmin(admin.ModelAdmin):
 list_display = ['banner_Abtimage1','banner_Abtimage2','banner_Abtimage3','aboutheading','banner_carAboutImage1','banner_carAboutImage2',
 'banner_carAboutImage3','banner_carAboutImage4','banner_carAboutImage5','banner_carAboutImage6','banner_carAboutImage5','Aboutbody']


@admin.register(PostService)
class ServiceAdmin(admin.ModelAdmin):
 list_display = ['Service_heading','banner_serv1','banner_serv2','banner_serv3','Servicebody']


@admin.register(PostVision)
class VisionAdmin(admin.ModelAdmin):
 list_display = ['banner_Visimage1','banner_Visimage2','banner_Visimage3','Vision_heading','Visionbody']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['Name','Email','Mobile','Target','Address','Message']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
 list_display = ['Name','Email','Mobile','Target','Address','Message']

@admin.register(Refferal)
class ReferralAdmin(admin.ModelAdmin):
 list_display = ['Name','Email','Mobile','Target','Address','Message']

@admin.register(quickuser)
class quickAdmin(admin.ModelAdmin):
 list_display = ['name','email','message']