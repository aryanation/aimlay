from adminapp.forms import HomeForm
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from app.models import Customer, PostHome, PostAbout, PostService, PostVision, Student, Business, Refferal
from app.forms import EditForm, RefferalForm, BusinessForm, CandidateForm
from django.urls import reverse_lazy
from .forms import PostHome, HomeForm, AboutForm, ServiceForm, VisionForm

#admin start customer detail

class Admin(ListView):
 model = Customer
 template_name = 'admin.html'

class detailCustomer(DetailView):
 model = Customer
 template_name = 'detail.html'


class updateAdmin(UpdateView):
 model = Customer
 form_class = EditForm
 template_name = 'updateadmin.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')


class DeleteAdmin(DeleteView):
 model = Customer
 template_name = 'deleteCustomer.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

#admin end customer detail


# start home

class HomePost(CreateView):
      model = PostHome
      form_class = HomeForm
      template_name = 'posthome.html'
      def get_success_url(self):
       return reverse_lazy('dashboard')

class Homeview(ListView):
      model = PostHome
      template_name = 'show/homeview.html'
      def get_success_url(self):
       return reverse_lazy('dashboard')

class Homeupdate(UpdateView):
      model = PostHome
      form_class = HomeForm
      template_name = 'updateshow/homeupdate.html'
      def get_success_url(self):
       return reverse_lazy('dashboard')

class Homedelete(DeleteView):
 model = PostHome
 template_name = 'deletepost/deletehome.html'
 success_url = 'admin'
 def get_success_url(self):
      return reverse_lazy('dashboard')

# end home


#start about
class AboutPost(CreateView):
      model = PostAbout
      form_class = VisionForm
      template_name = 'postabout.html'

class Aboutview(ListView):
      model = PostAbout
      template_name = 'show/aboutview.html'

class Aboutupdate(UpdateView):
      model = PostAbout
      form_class = AboutForm
      template_name = 'updateshow/aboutupdate.html'
      def get_success_url(self):
       return reverse_lazy('dashboard')
      

class Aboutdelete(DeleteView):
 model = PostAbout
 template_name = 'deletepost/deleteabout.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

#end about


#start vision
class VisionPost(CreateView):
 model = PostVision
 form_class = VisionForm
 template_name = 'postvision.html'

class Visionview(ListView):
 model = PostVision
 template_name = 'show/visionview.html'

class Visionupdate(UpdateView):
 model = PostVision
 form_class = VisionForm
 template_name = 'updateshow/visionupdate.html'
      

class Visiondelete(DeleteView):
 model = PostVision
 template_name = 'deletepost/deletevision.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

# end vision


      
class ServicePost(CreateView):
 model = PostService
 form_class = ServiceForm
 template_name = 'postservice.html'


class Serviceview(ListView):
 model = PostService
 template_name = 'show/serviceview.html'

class Serviceupdate(UpdateView):
 model = PostVision
 form_class = VisionForm
 template_name = 'updateshow/serviceupdate.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')
      

class Servicedelete(DeleteView):
 model = PostVision
 template_name = 'deletepost/deleteservice.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')


#student 

class Studentview(ListView):
      model = Student
      template_name = 'candidate.html'

class Studentdelete(DeleteView):
 model = Student
 template_name = 'deletepost/deletestudent.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class studentupdate(UpdateView):
 model = Student
 form_class = CandidateForm
 template_name = 'updateshow/studentupdate.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')


#end student

#referral


class referralview(ListView):
      model = Refferal
      template_name = 'referralAdmin.html'


class Refferaldelete(DeleteView):
 model = Refferal
 template_name = 'deletepost/deleteReferral.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class Refferalupdate(UpdateView):
 model = Refferal
 form_class = RefferalForm
 template_name = 'updateshow/updateref.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class businessview(ListView):
      model = Business
      template_name = 'busiAdmin.html'


class Businessdelete(DeleteView):
 model = Business
 template_name = 'deletepost/deletebusiness.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class Businessupdate(UpdateView):
 model = Business
 form_class = BusinessForm
 template_name = 'updateshow/businessupdate.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')


 

def profile(request):
 return render(request, 'profile.html')


def setting(request):
 return render(request, 'setting.html')