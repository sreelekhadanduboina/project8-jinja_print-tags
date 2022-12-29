from django.urls import path
from app1.views import *
app_name='somthing1'

urlpatterns = [
    path('htmlfile1/',htmlfile1,name='htmlfile1'),
]

