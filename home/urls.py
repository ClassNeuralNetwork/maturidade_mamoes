
from django.urls import path
from .views import train_papaya_view, verify_papaya_view, verify_papaya_dynamic_view

urlpatterns = [
    path('train-papaya/', train_papaya_view, name='train_papaya'),
    path('', verify_papaya_view, name='verify_papaya_view'),
    path('dynamic/', verify_papaya_dynamic_view, name='verify_papaya_dynamic_view'),
    
]

