from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StoreSerializer, ClientSerializer, OperatorSerializer
from authmanager.serializers import UserSerializer
from .models import Client, Operator, Store
# Create your views here.

class NewOperatorAPIView(APIView):
    
   def post(self, request):
        store = request.data['store']
        department = request.data['department']

        #print("Store UUID Check: ", store)
        department = request.POST.get('department', 'operations')
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()

        store_obj = Store.objects.get(uuid=store)

        operator = Operator.objects.create(user=user_obj, store=store_obj, department=department)

        serializer = OperatorSerializer(operator)

        data = {}

        data["success"] = True
        data["message"] = "New Client Created"
        data["data"] = serializer.data

        return Response(data=data, status=status.HTTP_201_CREATED)



class NewClientAPIView(APIView):
    
   def post(self, request):
        timezone = request.POST.get('timezone', 'UTC')
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()

        client = Client.objects.create(user=user_obj, timezone=timezone)

        serializer = ClientSerializer(client)

        data = {}

        data["success"] = True
        data["message"] = "New Client Created"
        data["data"] = serializer.data

        return Response(data=data, status=status.HTTP_201_CREATED)



class NewStoreAPIView(APIView):


    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = StoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data = {}
            data["success"] = True
            data["message"] = "New Store, %s, is  created"% (serializer.validated_data["name"] )
            data["data"] = serializer.data
            
            return Response(data=data, status=status.HTTP_201_CREATED)

        data = {}
        data["success"] = False
        data["error"] = serializer.errors
        data["message"] = "New Store could NOT be Created"
        
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

