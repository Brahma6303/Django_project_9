from  django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('app2_first/',app2_first,name="app2_first"),

]