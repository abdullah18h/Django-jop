
from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.job_list ,name=''),
    path('job/', views.job_details ,name=''),
]
