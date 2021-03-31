from django.urls import path
from KALPANA import views
urlpatterns = [ 
    path('',views.home),
    path('demo/',views.chk),
    path('home/',views.homepage),
    path('lg/',views.lgn),
    path('rg/',views.reg),
]