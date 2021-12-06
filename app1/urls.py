from django.urls import path
from . import views
urlpatterns=[
    path('',views.fnform,name='home')
]