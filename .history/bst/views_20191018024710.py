from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,get_authorization_header, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser,JSONParser
from rest_framework import mixins,generics,viewsets,status
from rest_framework.decorators import api_view
from .serializers import *
from kea.settings import SECRET_KEY
from kea.settings import FCM_API_KEY
from kea.settings import FCM_SENDER_ID
from kea.settings import FCM_TEST_REG_ID
from kea.settings import LOG_PATH
from kea.settings import DATABASES
from .models import *
import jwt
import json
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import sqlite3
import treant
from binarytree import tree,heap,Node



