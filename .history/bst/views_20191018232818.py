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
 

class treedisplay(APIView):

    queryset= userdata.objects.all()
    serializer_class = userviewSerializer
    def get(self,request,user_id):
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
            print(data)
            tree= treant.tree(data)
    
            return Response(tree)
        
            
        else:
            return Response({'msg':'user not found!!'})

# class Node: 
#     # A utility function to create a new node 
#     def __init__(self, key): 
#         self.key = key 
#         self.left = None
#         self.right = None
    
# """ Creates a node with key as 'i'. If i is root,then 
#     it changes root. If parent of i is not created, then 
#     it creates parent first  
# """
# def createNode(parent, i, created, root): 

#     # If this node is already created 
#     if created[i] is not None: 
#         return

#     # Create a new node and set created[i] 
#     created[i] = Node(i) 

#     # If 'i' is root, change root pointer and return 
#     if parent[i] == -1: 
#         root[0] = created[i] # root[0] denotes root of the tree 
#         return

#     # If parent is not created, then create parent first 
#     if created[parent[i]] is None: 
#         createNode(parent, parent[i], created, root ) 

#     # Find parent pointer 
#     p = created[parent[i]] 

#     # If this is first child of parent 
#     if p.left is None: 
#         p.left = created[i] 
#     # If second child 
#     else: 
#         p.right = created[i] 


# # Creates tree from parent[0..n-1] and returns root of the 
# # created tree 
# def createTree(parent): 
#     n = len(parent) 
    
#     # Create and array created[] to keep track  
#     # of created nodes, initialize all entries as None 
#     created = [None for i in range(n+1)] 
    
#     root = [None] 
#     for i in range(n): 
#         createNode(parent, i, created, root) 

#     return root[0] 

# #Inorder traversal of tree 
# def inorder(root): 
#     if root is not None: 
#         inorder(root.left) 
#         print root.key, 
#         inorder(root.right) 

# # Driver Method 
# parent = [-1, 0, 0, 1, 1, 3, 5] 
# root = createTree(parent) 
# print "Inorder Traversal of constructed tree"
# inorder(root)            

    

