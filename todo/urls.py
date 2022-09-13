from django.urls import path
from .views import *

urlpatterns = [
    path('delete-task/<int:pk>/', TodoDelete.as_view(), name='delete-task'), #the detail page looks for a primary key so we set it to <int:pk>
    path('update-task/<int:pk>/', TodoUpdate.as_view(), name='update-task'), #the detail page looks for a primary key so we set it to <int:pk>
    path('create-task/', TodoCreate.as_view(), name='create-task'), #the detail page looks for a primary key so we set it to <int:pk>
    path('task/<int:pk>/', TodoDetail.as_view(), name='task'), #the detail page looks for a primary key so we set it to <int:pk>
    path('', TodoList.as_view(), name='tasks'),
]
