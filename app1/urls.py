from django.urls import path
from app1.views import *

app_name="app1"

urlpatterns=[
    path('app_response/',app_response,name="app_response"),
]