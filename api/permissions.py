from rest_framework.permissions import BasePermission,SAFE_METHODS
# local 
from .models import TaskGroup
class IsOwner(BasePermission):
      def has_object_permission(self, request, view, obj):
            return obj.owner ==request.user
class IsOwnerThisgroup(BasePermission):
      def has_object_permission(self, request, view, obj):
            group_id =request.data.get('group',None)
            if request.method in SAFE_METHODS:
                  return True
            if not group_id==None:
                  try:
                        global TaskInstance
                        TaskInstance = TaskGroup.objects.get(pk=group_id)
                  except TaskGroup.DoesNotExist:
                        return False
                  return TaskInstance.owner  == request.user
            return True
class OWNERGroup(BasePermission):
      def has_permission(self, request, view):
            try:
                  global TaskInstance
                  TaskInstance = TaskGroup.objects.get(pk=view.kwargs['pk'])
            except TaskGroup.DoesNotExist:
                  return False
            return TaskInstance.owner  == request.user


      