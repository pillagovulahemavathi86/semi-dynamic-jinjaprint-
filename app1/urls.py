from django.urls import path
from app1.views import *
app_name='something1'

urlpatterns=[
    path('jinjaprint/',jinjaprint,name='jinjaprint')
]