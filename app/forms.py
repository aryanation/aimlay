from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Customer, Student, Business, Refferal

class CustomerForm(forms.ModelForm):
 class Meta:
  model = Customer
  fields = ['name','email','target','address','city','zipcode','state','message']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'target': forms.Select(attrs={'class':'form-control'}),
   'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
   'city': forms.TextInput(attrs={'class':'form-control','placeholder':'enter your city name'}),
   'zipcode': forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your zipcode'}),
   'state':forms.Select(attrs={'class':'form-control','placeholder':'enter your state'}),
   'message':forms.Textarea(attrs={'class':'form-control','placeholder':'write your message here'})
  }


class EditForm(forms.ModelForm):
 class Meta:
  model = Customer
  fields = ['name','email','target','address']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'target': forms.Select(attrs={'class':'form-control'}),
   'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
  }

class CandidateForm(forms.ModelForm):
 class Meta:
  model = Student
  fields = ['Name','Email','Mobile','Target','Address','Message']
  widgets = {
   'Name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile or Whatsapp number'}),
   'Target': forms.Select(attrs={'class':'form-control'}),
   'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
   'Message' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your Message'})
  }
  

class BusinessForm(forms.ModelForm):
 class Meta:
  model = Business
  fields = ['Name','Email','Mobile','Target','Address','Message']
  widgets = {
   'Name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile or Whatsapp number'}),
   'Target': forms.Select(attrs={'class':'form-control'}),
   'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
   'Message' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your Message'})
  }


class RefferalForm(forms.ModelForm):
 class Meta:
  model = Refferal
  fields = ['Name','Email','Mobile','Target','Address','Message']
  widgets = {
   'Name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'Mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile or Whatsapp number'}),
   'Target': forms.Select(attrs={'class':'form-control'}),
   'Address': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
   'Message' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your Message'})
  }