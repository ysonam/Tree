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
      
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  

class Detail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, user_id):
        try:
            return userdata.objects.get(id=user_id)
        except userdata.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
       
        tree = treant.tree(list(snippet.data))
        
        serializer = userviewSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        snippet = self.get_object(user_id)
        serializer = userviewSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,user_id, format=None):
        snippet = self.get_object(user_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None          
 

class treedisplay(APIView):

    queryset= userdata.objects.all()
    serializer_class = userviewSerializer
    def get(self,request,user_id):
        # try:

        #     users = userdata.objects.get(id=user_id)
        # except Exception as e:
        #     users=None
        # if users:        
        #     array=  list(users.data)
        #     array=''.join(array)
    
        #     data=array.strip('][').split(', ') 
        #     print(data)
        #     data.sort(key=int)
        #     nums=data
        #     tree= treant.tree(data)
        # else:
        #     return Response({'msg':'user not found!!'})

        def sorted_array_to_bst(self,nums):
            try:

                users = userdata.objects.get(id=user_id)
            except Exception as e:
                users=None
            if users:        
                array=  list(users.data)
                array=''.join(array)
        
                data=array.strip('][').split(', ') 
                print(data)
                data.sort(key=int)
                nums=data
                tree= treant.tree(data)
            else:
                return Response({'msg':'user not found!!'})

    
        
            if not nums:
                return None
            mid_val = len(nums)//2
            node = TreeNode(nums[mid_val])
            node.left = sorted_array_to_bst(nums[:mid_val])
            node.right = sorted_array_to_bst(nums[mid_val+1:])
            return node
            
        def preOrder(self,node): 
            if not node: 
                return      
            print(node.val)
            preOrder(node.left) 
            preOrder(node.right)  
            

    #return Response({'msg':'user'})             



# def sorted_array_to_bst(nums):
#     if not nums:
#         return None
#     mid_val = len(nums)//2
#     node = TreeNode(nums[mid_val])
#     node.left = sorted_array_to_bst(nums[:mid_val])
#     node.right = sorted_array_to_bst(nums[mid_val+1:])
#     return node

# def preOrder(node): 
#     if not node: 
#         return      
#     print(node.val)
#     preOrder(node.left) 
#     preOrder(node.right)   


        
# result = sorted_array_to_bst([1,2,2])
# preOrder(result)        

    

