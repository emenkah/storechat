from django.urls import path
from .views import NewStoreAPIView, NewClientAPIView, NewOperatorAPIView

urlpatterns = [ 
    path('new-store/', NewStoreAPIView.as_view()),
    path('operator/new-operator/', NewOperatorAPIView.as_view()),
    path('customer/register/', NewClientAPIView.as_view()),
    

    

]