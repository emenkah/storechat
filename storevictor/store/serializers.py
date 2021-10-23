from rest_framework import serializers
from . models import Store, Client, User, Operator
from authmanager.serializers import UserSerializer



class StoreSerializer(serializers.ModelSerializer):

    created_by_details = UserSerializer(source='created_by', read_only=True)

    class Meta:
        model = Store
        fields = [ 'name', 'created_by', 'created_by_details', 'timezone', 'telephone']
        extra_kwargs = {
            'created_by': {'write_only': True} 
        }


class OperatorSerializer(serializers.ModelSerializer):
    
    operator_detail = UserSerializer(source='user', read_only=True)
    store_detail = StoreSerializer(source='store', read_only=True)

    class Meta:
        model = Operator
        dept = 1
        fields = [ 'user', 'store', 'store_detail', 'operator_detail', 'department' ]
        extra_kwargs = {
            'store': {'write_only': True} 
        }

class ClientSerializer(serializers.ModelSerializer):
    
    client_detail = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Client
        dept = 1
        fields = [ 'user', 'client_detail', 'timezone', 'address']


