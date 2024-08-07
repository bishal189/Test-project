from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.home,name='home'),
    path('signin/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('store/',views.store,name='store'),
]
