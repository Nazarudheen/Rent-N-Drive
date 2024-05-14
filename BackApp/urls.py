from django.urls import path
from BackApp import views

urlpatterns = [
    path('index/',views.Index_Page,name="Index_Page"),
    path('Add_Car/',views.Add_Car,name="Add_Car"),
    path('Save_car/',views.Save_car,name="Save_car"),
    path('Blog_Add/',views.Blog_Add,name="Blog_Add"),
    path('Blog_Display/',views.Blog_Display,name="Blog_Display"),
    path('Save_Blog/',views.Save_Blog,name="Save_Blog"),
    path('Bookings_page/',views.Bookings_page,name="Bookings_page"),
    path('DriverJob/',views.DriverJob,name="DriverJob"),
    path('FeedbackPage/',views.FeedbackPage,name="FeedbackPage"),
    path('LoginPage/',views.LoginPage,name="LoginPage"),
    path('Admin_login/',views.Admin_login,name="Admin_login"),

    path('Display_car/',views.Display_car,name="Display_car"),
    path('Edit_Page/<int:cid>/',views.Edit_Page,name="Edit_Page"),
    path('Update_car/<int:cid>/', views.Update_car, name="Update_car"),
    path('delete_car/<int:cid>/', views.delete_car, name="delete_car"),
    path('delete_feed/<int:fid>/', views.delete_feed, name="delete_feed"),

    path('Save_driver/',views.Save_driver,name="Save_driver"),
    path('Driver_Display/',views.Driver_Display,name="Driver_Display"),
    path('Driver_Add/',views.Driver_Add,name="Driver_Add"),
    path('DisplayEditDelete_car/',views.DisplayEditDelete_car,name="DisplayEditDelete_car"),
    path('Edit_Driver/<int:did>/',views.Edit_Driver,name="Edit_Driver"),
    path('Update_Driver/<int:did>/',views.Update_Driver,name="Update_Driver"),
    path('delete_driver/<int:did>/',views.delete_driver,name="delete_driver"),
]