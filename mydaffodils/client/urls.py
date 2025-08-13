from django.urls import path
from client import views

urlpatterns=[ 
path("",views.index,name="home"),
path('contact/', views.contact, name='contact'),
path('about/',views.about,name="about"),
path('project/',views.project,name="project"),
path('thankyou/',views.thankyou,name="thankyou"),
]