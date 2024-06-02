from django.contrib import admin

# local 
from .models import Task,TaskGroup
# Register your models here.
admin.site.register(Task)
admin.site.register(TaskGroup)
