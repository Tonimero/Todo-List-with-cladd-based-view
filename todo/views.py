from django.shortcuts import render
from django.views.generic.list import ListView

from todo.models import * #imports all the models from the models.py file

# Create your views here.
class listView(ListView): #ListView contains functionalities that reqrns a query set of data
    model = Task
    context_object_name = 'tasks' #changes the default Object_list that gets all the objects from the data base to task