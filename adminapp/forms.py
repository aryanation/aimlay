from ckeditor.fields import RichTextField
from django import forms
from django.db.models import fields
from django.forms import widgets
from app.models import PostAbout, PostHome, PostService, PostVision
from ckeditor.fields import RichTextField


class HomeForm(forms.ModelForm):
 class Meta:
  model = PostHome
  fields = ['banner_homeImage1','banner_homeImage2','banner_homeImage3','banner_review_image1','banner_review_image2','banner_review_image3']




class AboutForm(forms.ModelForm):
 class Meta:
  model = PostAbout
  fields = ['banner_Abtimage1','banner_Abtimage2','banner_Abtimage3','aboutheading','banner_carAboutImage1','banner_carAboutImage2','banner_carAboutImage3','banner_carAboutImage4','banner_carAboutImage5','Aboutbody']
  widgets = {
   'aboutheading': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Aboutbody': RichTextField()
   }


class VisionForm(forms.ModelForm):
 class Meta:
  model = PostVision
  fields = ['banner_Visimage1','banner_Visimage2','banner_Visimage3','Vision_heading', 'Visionbody']
  widgets = {
   'Vision_heading': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Visionbody': RichTextField()
   }

class ServiceForm(forms.ModelForm):
 class Meta:
  model = PostService
  fields = ['Service_heading','banner_serv1','banner_serv2','banner_serv3','Servicebody']
  widgets = {
   'Service_heading': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Servicebody': RichTextField()
   }