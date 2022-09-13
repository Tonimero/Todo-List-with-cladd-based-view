from django.shortcuts import render
from django.views.generic.list import ListView #like the homepage. like objects.a()
from django.views.generic.detail import DetailView #like the detail page. like get_object_or _404
from django.views.generic.edit import CreateView, UpdateView, DeleteView #this view Creates a post. C in CRUD
from django.urls import reverse_lazy #handles redirect


from todo.models import * #imports all the models from the models.py file

# Create your views here.
class TodoList(ListView): #ListView contains functionalities that reqrns a query set of data
    model = Task
    context_object_name = 'tasks' #changes the default Object_list that gets all the objects from the data base to task

class TodoDetail(DetailView):
    model = Task    
    context_object_name = 'task'
    template_name = 'todo/task.html'

class TodoCreate(CreateView): #Create view uses a model form. By default, the CreateView gves us a model form to work with
    model = Task
    template_name = 'todo/create.html'
    fields = '__all__' #this brings out all the fields from the model and renders it to the create form
    success_url = reverse_lazy('tasks') #back to the homepage

class TodoUpdate(UpdateView): #Create view uses a model form. By default, the CreateView gves us a model form to work with
    model = Task
    template_name = 'todo/update.html'
    fields = '__all__' #this brings out all the fields from the model and renders it to the create form
    success_url = reverse_lazy('tasks') #back to the homepage

class TodoDelete(DeleteView): #Create view uses a model form. By default, the CreateView gves us a model form to work with
    model = Task
    template_name = 'todo/delete.html'
    fields = '__all__' #this brings out all the fields from the model and renders it to the create form
    success_url = reverse_lazy('tasks') #back to the homepage






    