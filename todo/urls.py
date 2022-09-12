from django.urls import path
from .views import *

urlpatterns = [
    path('', listView.as_view(), name='task')
]
