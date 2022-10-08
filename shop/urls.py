from django.urls import path
from shop.views import details, index, checkout, confirmation

urlpatterns = [
    path('', index, name="index"),
    path('<int:id>', details, name="details"),   #url dynamique qui change en fonction de la valeur de id
    path('checkout', checkout, name="checkout"), 
    path('confirmation', confirmation, name="confirmation"),  
]