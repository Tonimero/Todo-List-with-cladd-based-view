from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic.list import ListView #like the homepage. like objects.a()
from django.views.generic.detail import DetailView #like the detail page. like get_object_or _404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView #(form view helps with regitration of user) #this view Creates a post. C in CRUD
from django.urls import reverse_lazy #handles redirect

from django.contrib.auth.views import LoginView #this handles all functionalties pertaining to login of a user

#Add the LoginRequiredMixin to each views to restrict un    uthorized access
from django.contrib.auth.mixins import LoginRequiredMixin #restricts a user from viewing a page if he isnt logged in. Go to the settings.py to override  the misims
from django.contrib.auth.forms import UserCreationForm #once the registration form is created, it authomatically creates a user for us
from django.contrib.auth import login

from todo.models import * #imports all the models from the models.py file

# Create your views here.
#place the login on top of the views
class loginUser(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__' 
    redirect_authenticated_user = True #if a user is logged in or authenticated, they should be redirected to the todo page

    def get_success_url(self):
        return reverse_lazy('tasks') #when a user logs in, the user is sent to the todo page


class RegisterUser(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks') #redirects the registered user to the todo page
    
    def form_valid(self, form):
    #when the user clicks register
        user = form.save() #saves the form
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUser, self).get(*args, **kwargs)


class TodoList(LoginRequiredMixin, ListView): #ListView contains functionalities that reqrns a query set of data
    model = Task
    context_object_name = 'tasks' #changes the default Object_list that gets all the objects from the data base to task

    #to ensure that a user only gets his own task and not other users' task
    #we make use of get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user) #this assigns a task to only a user and invisiblw to other users
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Task    
    context_object_name = 'task'
    template_name = 'todo/task.html'

class TodoCreate(LoginRequiredMixin, CreateView): #Create view uses a model form. By default, the CreateView gives us a model form to work with
    model = Task
    template_name = 'todo/create.html'
    fields = ['title', 'description', 'complete'] #this brings out all the fields from the model and renders it to the create form
    success_url = reverse_lazy('tasks') #back to the homepage
    
    def form_valid(self, form):
        form.instance.user = self.request.user #making sure the logged in user doesnt see other users when creating tasks
        return super(TodoCreate, self).form_valid(form)



class TodoUpdate(LoginRequiredMixin, UpdateView): #Create view uses a model form. By default, the CreateView gves us a model form to work with
    model = Task
    template_name = 'todo/update.html'
    fields = ['title', 'description', 'complete'] # -----> #this brings out all the fields from the model and renders it to the create form ----- NOTE: '__all__' (shows all the fields in the model)
    success_url = reverse_lazy('tasks') #back to the homepage

class TodoDelete(LoginRequiredMixin, DeleteView): #Create view uses a model form. By default, the CreateView gves us a model form to work with
    model = Task
    template_name = 'todo/delete.html'
    # fields = '__all__' #this brings out all the fields from the model and renders it to the create form
    success_url = reverse_lazy('tasks') #back to the homepage





    