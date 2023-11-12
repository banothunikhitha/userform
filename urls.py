# userform/urls.py
from django.urls import path
from .views import user_form, user_data

urlpatterns = [
    path('userform/', user_form, name='user_form'),
    path('userdata/', user_data, name='user_data'),
]
