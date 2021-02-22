from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from django.views.generic import ListView
from .forms import CustomerForm, RefferalForm, BusinessForm, CandidateForm
from .models import Customer, PostAbout, PostHome,Student, Refferal, Business, quickuser
from django.urls import reverse_lazy

class home(ListView):
 model = PostHome
 template_name = 'index.html'
 def get_success_url(self):
      return reverse_lazy('home')
 
def extract(request):
 
 nm = request.POST['name']
 em = request.POST['email']
 msg = request.POST['email-message']
 userinfo = quickuser(name=nm, email=em, message=msg)
 userinfo.save()
 return(request, 'index.html')


class referral(CreateView):
 model = Refferal
 form_class = RefferalForm
 template_name = 'referral.html'
 def get_success_url(self):
      return reverse_lazy('ref')


class student(CreateView):
 model = Student
 form_class = CandidateForm
 template_name = 'student.html'
 def get_success_url(self):
      return reverse_lazy('student')


class business(CreateView):
 model = Business
 form_class = BusinessForm
 template_name = 'business_partner.html'
 def get_success_url(self):
      return reverse_lazy('business')


class about(ListView):
 model = PostAbout
 template_name = 'about.html'
 def get_success_url(self):
      return reverse_lazy('about')



def vision(request):
 return render(request, 'vision.html')


def services(request):
 return render(request, 'service.html')


# def contact(request):
 # return render(request, 'contact.html')

class contact(CreateView):
 model = Customer
 form_class = CustomerForm
 template_name = 'contact.html'

def join(request):
 return render(request, 'join.html')


class Query(CreateView):
 model = Customer
 form_class = CustomerForm
 template_name = 'form.html'

 
 