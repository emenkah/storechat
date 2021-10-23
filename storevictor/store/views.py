from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StoreSerializer, ClientSerializer, OperatorSerializer, ConversationPartySerializer
from authmanager.serializers import UserSerializer
from .models import Client, Operator, Store, ConversationParty
# Create your views here.

class NewConversationPartyAPIView(APIView):

    def get(self, request):
        services = ConversationParty.objects.all()
        serializer = ConversationPartySerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = ConversationPartySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {}

        data["success"] = True
        data["message"] = "New Client Created"
        data["data"] = serializer.data

        return Response(data=data, status=status.HTTP_201_CREATED)



class NewConversationPartyDetailsAPIView(APIView):

    def get_object(self, uuid):

        try:            
            convo_party = get_object_or_404(ConversationParty, uuid=uuid, is_deleted=False)
            return convo_party
            
        except ConversationParty.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, uuid):
        convo_party = self.get_object(uuid)
        serializer = ConversationPartySerializer(convo_party)
        return Response(serializer.data)

    def put(self, request, uuid):

        service = self.get_object(uuid)
        serializer = ConversationPartySerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, uuid): 
        convo_party = self.get_object(uuid)
        convo_party.is_deleted = True
        convo_party.save()
        return  Response(status=status.HTTP_204_NO_CONTENT)


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

