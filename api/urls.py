from django.urls import path
from . import views
urlpatterns =[
      path('tasks',views.ListCreateTask.as_view()),
      path('tasks/<int:pk>',views.RetriveUpdateDeleteTask.as_view(),name='task'),
      path('groups',views.ListCreateGroup.as_view()),
      path('groups/<int:pk>',views.RetriveUpdateDeleteGroup.as_view()),
      path('groups/<int:pk>/tasks',views.ListTasksOfGroup),
      path('groups/<int:pk>/tasks/delete',views.RemoveAllTaskOfGroup),
      path('groups/<int:pk>/tasks/<int:tpk>',views.TaskForGroup)
]