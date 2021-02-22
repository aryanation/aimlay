from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
STATE_CHOICES = (
 ('Andaman & Nicobar Island','Andaman & Nicobar Island'),('Andhra Pardesh','Andhra Pardesh'), 
 ('Arunachal Pardesh','Arunachal Pardesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattishgarh','Chhattishgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi', 'Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pardesh','Himachal Pardesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Lakshadweep','Lakshadweep'),
  ('MAdhya Pardesh','MAdhya Pardesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalya','Meghalya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Pondicherry','Pondicherry'),
  ('Punjab','Punjab'),
  ('Rajashthan','Rajashthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pardesh','Uttar Pardesh'),
  ('West Bengal','West Bengal')
)


TARGET_GROUP = (
 ('Candidate','Candidate'),
 ('Referral','Referral'),
 ('Business_Partner','Business_Partner'),
)

class Customer(models.Model):
 name = models.CharField(max_length=50)
 email= models.EmailField(max_length=254)
 address = models.CharField(max_length=50)
 city = models.CharField(max_length=50)
 target = models.CharField(choices=TARGET_GROUP, max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES,max_length=50)
 message = models.TextField()

 def __str__(self):
     return str(self.id)
  
 def get_absolute_url(self):
      return reverse('home')


class PostHome(models.Model):
  banner_homeImage1 =cloudinary.models.CloudinaryField('image')
  banner_homeImage2 =cloudinary.models.CloudinaryField('image')
  banner_homeImage3 =cloudinary.models.CloudinaryField('image')
  banner_review_image1 =cloudinary.models.CloudinaryField('image')
  banner_review_image2 =cloudinary.models.CloudinaryField('image')
  banner_review_image3 =cloudinary.models.CloudinaryField('image')

  def __str__(self):
      return str()


class PostAbout(models.Model):
  banner_Abtimage1 =cloudinary.models.CloudinaryField('image')
  banner_Abtimage2 =cloudinary.models.CloudinaryField('image')
  banner_Abtimage3 =cloudinary.models.CloudinaryField('image')
  aboutheading = models.CharField( max_length=50)
  banner_carAboutImage1 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage2 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage3 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage4 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage5 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage6 =cloudinary.models.CloudinaryField('image')
  banner_carAboutImage7 =cloudinary.models.CloudinaryField('image')
  Aboutbody = RichTextField()

  def __str__(self):
      return str(self.id)


class PostService(models.Model):
  Service_heading = models.CharField( max_length=50)
  banner_serv1 =cloudinary.models.CloudinaryField('image')
  banner_serv2 =cloudinary.models.CloudinaryField('image')
  banner_serv3 =cloudinary.models.CloudinaryField('image')
  Servicebody = RichTextField()
  def __str__(self):
      return str(self.id)


class PostVision(models.Model):
  banner_Visimage1 =cloudinary.models.CloudinaryField('image')
  banner_Visimage2 =cloudinary.models.CloudinaryField('image')
  banner_Visimage3 =cloudinary.models.CloudinaryField('image')
  Vision_heading = models.CharField( max_length=50)
  Visionbody = RichTextField() 
  
  def __str__(self):
      return str(self.id)

CANDIDATE_GROUP = (
 ('Candidate','Candidate'),
)

class Student(models.Model):
  Name = models.CharField(max_length=50)
  Email = models.EmailField(max_length=254)
  Mobile = models.IntegerField()
  Target = models.CharField(choices=CANDIDATE_GROUP, max_length=50, default=None)
  Address = models.CharField(max_length=50)
  Message = models.TextField()


BUSINESS_GROUP = (
 ('Business_Partner','Business_Partner'),
)
  
class Business(models.Model):
  Name = models.CharField(max_length=50)
  Email = models.EmailField(max_length=254)
  Mobile = models.IntegerField()
  Target = models.CharField(choices=BUSINESS_GROUP, max_length=50, default=None)
  Address = models.CharField(max_length=50)
  Message = models.TextField()



REFERRAL_GROUP = (
 ('Referral','Referral'),
)



class Refferal(models.Model):
  Name = models.CharField(max_length=50)
  Email = models.EmailField(max_length=254)
  Mobile = models.IntegerField()
  Target = models.CharField(choices=REFERRAL_GROUP, max_length=50, default=None)
  Address = models.CharField(max_length=50)
  Message = models.TextField()


class quickuser(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  message = models.TextField()