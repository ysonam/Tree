from rest_framework import serializers
from . models import *

class userviewSerializer(serializers.ModelSerializer):
    data =serializers.ListField()
    class Meta:
        model = userdata
        fields = ('id,'data',)