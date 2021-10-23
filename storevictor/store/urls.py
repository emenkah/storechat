from django.urls import path
from .views import ( NewStoreAPIView, NewClientAPIView, NewOperatorAPIView, 
                    NewConversationPartyAPIView, NewConversationPartyDetailsAPIView
)

urlpatterns = [ 
    path('new-store/', NewStoreAPIView.as_view()),
    path('operator/new-operator/', NewOperatorAPIView.as_view()),
    path('customer/register/', NewClientAPIView.as_view()),
    path('customer/register/', NewClientAPIView.as_view()), 
    path('operation/conversation/', NewConversationPartyAPIView.as_view()), 
    path('operation/conversation/<uuid>/', NewConversationPartyDetailsAPIView.as_view()), 

]