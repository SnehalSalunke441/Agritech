from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginuser, name="login"),
    path("signup",views.signup, name='signup'),
    path('logout',views.logoutuser, name="logout"),
    path("about",views.about, name='about'),
    path("crops",views.crops, name='crops'),
    path("pesticides",views.pesticides, name='pesticides'),
    path("fertilizers",views.fertilizers, name='fertilizers'),
    path("moderntech",views.moderntech, name='moderntech'),
    path("wheat",views.wheat, name='wheat'),
    path("rice",views.rice, name='rice'),
    path("onion",views.onion, name='onion'),
    path("marigold",views.marigold, name='marigold'),
    path("orange",views.orange, name='orange'),
    path("corn",views.corn, name='corn'),
    path("contact",views.contact, name='contact'),
    path("landing",views.landing, name='landing'),
    path("urea",views.urea, name='urea'),
    path("nitrophosphate",views.nitrophosphate, name='nitrophosphate'),
    path("dap",views.dap, name='dap'),
    path("ssp",views.ssp, name='ssp'),
    path("herbicides",views.herbicides, name='herbicides'),
    path("insecticides",views.insecticides, name='insecticides'),
    path("fungicides",views.fungicides, name='fungicides'),
    path("indoorvp",views.indoorvp, name='indoorvp'),
    path("farmauto",views.farmauto, name='farmauto'),
    path("greenhousefarm",views.greenhousefarm, name='greenhousefarm'),

]
