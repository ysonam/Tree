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
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class add_data(generics.CreateAPIView):
    queryset= userdata.objects.all()
    serializer_class = userviewSerializer
    model= userdata
    def post(self,request,format=None):
       
        serializer = userviewSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            

            return Response(serializer.data)
        return Response(serializer.errors)

    def get_object(self):
        try:
            if 'user_id' in request.GET and request.GET['user_id']:
                user_id = request.GET['user_id']
                return userdata.objects.get(id=user_id)
            return Response({'msg':'invalid id'})    
        except userdata.DoesNotExist:
            raise Http404    

    def get(self, request,format=None):
        print(request.data)
        if 'user_id' in request.GET and request.GET['user_id']:
            user_id = request.GET['user_id']
            data = userdata.objects.get(id=user_id)
            # print(data.data)
            # snippet = self.get_object(user_id)
            # print(snippet)
            serializer = userviewSerializer(data)
            return Response(serializer.data)

    # def put(self, request, format=None):
    #     if 'user_id' in request.data and request.data['user_id']:
    #         user_id = request.data['user_id']
    #         snippet = self.get_object(user_id)
    #         serializer = userviewSerializer(snippet, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, format=None):
    #     if 'user_id' in request.data and request.data['user_id']:
    #         user_id = request.data['user_id']
    #         snippet = self.get_object(user_id)
    #         snippet.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)   

    
    
    

