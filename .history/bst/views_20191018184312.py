from django.shortcuts import render, HttpResponse
from rest_framework_jwt.settings import api_settings
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from rest_framework.decorators import api_view
from .serializers import *
from tree.settings import DATABASES
from .models import *
from django.http import Http404,JsonResponse
from django.db.models import Q
from django.core import serializers
from django.core.exceptions import ValidationError
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
import sqlite3
import treant
from binarytree import tree,heap,Node

class add_data(generics.CreateAPIView):

    queryset= userdata.objects.all()
    serializer_class = userviewSerializer
    
    def post(self,request,format=None):
        
        serializer = userviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

