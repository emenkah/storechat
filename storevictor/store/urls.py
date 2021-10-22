from django.urls import path
from .views import NewClientAPIView

urlpatterns = [ 
    path('customer/register/', NewClientAPIView.as_view()),
    

]