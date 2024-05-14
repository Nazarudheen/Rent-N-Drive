from django.urls import path
from FrontApp import views


urlpatterns=[
    path('Home/',views.IndexPage,name="IndexPage"),
    path('AboutPage/',views.AboutPage,name="AboutPage"),
    path('BlogPage/',views.BlogPage,name="BlogPage"),
    path('CarPage/',views.CarPage,name="CarPage"),
    path('ContactPage/',views.ContactPage,name="ContactPage"),
    path('PricePage/',views.PricePage,name="PricePage"),
    path('ServicePage/',views.ServicePage,name="ServicePage"),
    path('SaveContact/',views.SaveContact,name="SaveContact"),
    path('a/',views.SignupSigninpage,name="SignupSigninpage"),
    path('SignupPage/',views.SignupPage,name="SignupPage"),
    path('LoginUser/',views.LoginUser,name="LoginUser"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('BookingPage/<int:bkid>/',views.BookingPage,name="BookingPage"),
    path('SaveBooking/',views.SaveBooking,name="SaveBooking"),
    path('DriverFormPage/',views.DriverFormPage,name="DriverFormPage"),
    path('DriverJobSave/',views.DriverJobSave,name="DriverJobSave"),
    path('Paymentpage/',views.Paymentpage,name="Paymentpage"),
    path('CarSingle/<int:scid>/',views.CarSingle,name="CarSingle"),
    path('BlogSingle/<int:bid>/',views.BlogSingle,name="BlogSingle"),


    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('abc', views.homepage, name='index'),



]