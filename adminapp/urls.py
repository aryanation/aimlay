from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

 path('admin/', views.Admin.as_view(), name='dashboard'),
 path('homepost/', views.HomePost.as_view(), name='homepost'),
 path('visionpost/', views.VisionPost.as_view(), name='visionpost'),
 path('aboutpost/', views.AboutPost.as_view(), name='aboutpost'),
 path('servicepost/', views.ServicePost.as_view(), name='servicepost'),
 path('homeview/', views.Homeview.as_view(), name='homeview'),
 path('updatehome/<int:pk>', views.Homeupdate.as_view(), name='updatehome'),
 path('deletehome/<int:pk>', views.Homedelete.as_view(), name='deletehome'),
 path('aboutview/', views.Aboutview.as_view(), name='aboutview'),
 path('updateabout/<int:pk>', views.Aboutupdate.as_view(), name='updateabout'),
 path('deleteabout/<int:pk>', views.Aboutdelete.as_view(), name='deleteabout'),
 path('visionview/', views.Visionview.as_view(), name='visionview'),
 path('updatevision/<int:pk>', views.Visionupdate.as_view(), name='updatevision'),
 path('deletevision/<int:pk>', views.Visiondelete.as_view(), name='deletevision'),
 path('serviceview/', views.Serviceview.as_view(), name='serviceview'),
 path('updateservice/<int:pk>', views.Serviceupdate.as_view(), name='updateservice'),
 path('deleteservice/<int:pk>', views.Servicedelete.as_view(), name='deleteservice'),
 path('busiAdmin/', views.businessview.as_view(), name='busiAdmin'),
 path('deletebusiness/<int:pk>', views.Businessdelete.as_view(), name='deletebusiness'),
 path('updatebusiness/<int:pk>', views.Businessupdate.as_view(), name='updatebusiness'),
 path('referral/', views.referralview.as_view(), name='referral'),
 path('deletereferral/<int:pk>', views.referralview.as_view(), name='deleteref'),
 path('updatereferral/<int:pk>', views.referralview.as_view(), name='updateref'),
 path('candidate/', views.Studentview.as_view(), name='candidate'),
 path('deletestudent/<int:pk>', views.Studentdelete.as_view(), name='deletestudent'),
 path('updatestudent/<int:pk>', views.studentupdate.as_view(), name='updatestudent'),
 path('pro/', views.profile, name='profile'),
 path('sets/', views.setting, name='setting'),
 path('update/<int:pk>', views.updateAdmin.as_view(), name='update'),
 path('detailCustomer/<int:pk>', views.detailCustomer.as_view(), name='detailCustomer'),
 path('deleteCustomer/<int:pk>', views.DeleteAdmin.as_view(), name='detelecustomer'),
 path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='reset_password'),

]
