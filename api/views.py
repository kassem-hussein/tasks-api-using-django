from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework  import generics
# local 
from .models import Task,TaskGroup
from .serializers import TaskSerializer,TaskGroupserializer
from .permissions import IsOwner,OWNERGroup,IsOwnerThisgroup
class ListCreateTask(generics.ListCreateAPIView):
      permission_classes =[IsAuthenticated]
      queryset =Task.objects.all()
      serializer_class =TaskSerializer
      def get_queryset(self):
            return Task.objects.filter(owner=self.request.user)
class RetriveUpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
      queryset =Task.objects.all()
      serializer_class =TaskSerializer
      permission_classes =[IsAuthenticated,IsOwner,IsOwnerThisgroup]
      def get_queryset(self):
                return Task.objects.filter(owner=self.request.user)

@api_view(['GET'])
@permission_classes([OWNERGroup])
def ListTasksOfGroup(request,pk):
      instance =Task.objects.filter(group_id=pk)
      serializer =TaskSerializer(instance,many=True)
      return Response(serializer.data,status=200)
@api_view(['DELETE'])
@permission_classes([OWNERGroup])     
def RemoveAllTaskOfGroup(request,pk) :
      try:
            instances =Task.objects.filter(group_id=pk)
            for obj in instances:
                  obj.delete()
            return Response({'message':'Deleted all Task to this group successfuly'},status=204)
      except Task.DoesNotExist:
            return Response({'message':'messing group id or group id not correct'},status=400)
      
# class TaskForGroup(generics.RetrieveUpdateDestroyAPIView):
#       queryset =Task.objects.all()
#       serializer_class =TaskSerializer
#       permission_classes= [OWNERGroup]
#       def get_queryset(self):
#             return Task.objects.get(pk=self.kwargs.get('tpk',0 ))
@api_view(['GET'])
@permission_classes([OWNERGroup])
def TaskForGroup(request,pk,tpk):
      if request.method =='GET':
            instance =Task.objects.get(pk=tpk,group__id=pk)
            serializer =TaskSerializer(instance)
            return Response(serializer.data,status=200)
     


      
class ListCreateGroup(generics.ListCreateAPIView):
      queryset =TaskGroup.objects.all()
      serializer_class =TaskGroupserializer
      permission_classes =[IsAuthenticated]
      def  get_queryset(self):
            return TaskGroup.objects.filter(owner=self.request.user)
class RetriveUpdateDeleteGroup(generics.RetrieveUpdateDestroyAPIView):
      queryset =TaskGroup.objects.all()
      serializer_class =TaskGroupserializer
      permission_classes =[IsOwner]
