from django.db import models
from django.contrib.auth.models import User #takes care of the user authentication like email password etc

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #setting the many-to-one relationship where the user can have many items using a foreign key
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['complete'] #orders by the complete status of the added item
    