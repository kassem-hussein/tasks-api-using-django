from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskGroup(models.Model):
      owner        = models.ForeignKey(User,on_delete=models.CASCADE)
      title        = models.CharField(max_length=255)
      def __str__(self):
                return self.title
      
      
class Task(models.Model):
      owner        = models.ForeignKey(User, on_delete=models.CASCADE)
      title        = models.CharField(max_length=255)
      description  = models.TextField()
      group        = models.ForeignKey(TaskGroup,related_name='Tasks',on_delete=models.SET_NULL,blank=True,null=True)
      def __str__(self):
            return self.title


