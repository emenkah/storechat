from rest_framework import serializers
from . models import Store, Client, User
from authmanager.serializers import UserSerializer



class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = [ 'name', 'created_by', 'timezone', 'telephone']


class ClientSerializer(serializers.ModelSerializer):
    
    client_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Client
        dept = 1
        fields = [ 'user', 'client_detail', 'timezone', 'address']


