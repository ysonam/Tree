from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from rest_framework_jwt.views import (obtain_jwt_token,
                                        verify_jwt_token,
                                        refresh_jwt_token)
from rest_framework.urlpatterns import format_suffix_patterns
from bst import views


app_name = "bst"

urlpatterns=[
    path('user_data/', views.add_data.as_view()),
    
]