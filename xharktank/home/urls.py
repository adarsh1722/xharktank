from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path('' ,  views.home, name = "home"),
    path('pitches', views.PostPitches, name = "allPitches"),
    path('pitches/<int:pk>', views.Get, name = "singlePitch"),
    path('pitches/<int:pk>/makeOffer' , views.MakeOffer, name = "makeOffer")
]