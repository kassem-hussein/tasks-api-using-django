from  rest_framework import serializers
from rest_framework.response import Response
# local 
from .models import Task,TaskGroup
class GroupTaskSerializer(serializers.ModelSerializer):
      owner  = serializers.SerializerMethodField()
      class Meta:
            model =TaskGroup
            fields =['id','title','owner','Tasks']
      def get_owner(self,obj):
            return obj.owner.username
class TaskGroupserializer(serializers.ModelSerializer):
      owner  = serializers.SerializerMethodField()
      class Meta:
            model =TaskGroup
            fields =['id','title','owner']
      def get_owner(self,obj):
            return obj.owner.username
      def create(self, validated_data):
            owner  =self.context['request'].user
            return TaskGroup.objects.create(owner=owner,**validated_data)
class TaskSerializer(serializers.ModelSerializer):
      owner = serializers.SerializerMethodField()
      group = serializers.SerializerMethodField()
      class Meta:
            model =Task
            fields =['id','title','description','owner','group']
      def get_owner(self,obj):
            return obj.owner.username
      def get_group(self,obj):
            if not obj.group ==  None:
                  return obj.group.title
      def create(self,validated_data):
        owner  =self.context['request'].user
        group_id  =self.context['request'].data.get('group','')

        if not group_id == '':
            try:
                  global group
                  group =TaskGroup.objects.get(id=group_id)

                  if not group.owner == owner:
                      raise serializers.ValidationError({'message':f'you are not autherized to this group'},403)
                         
            except TaskGroup.DoesNotExist:
                  raise serializers.ValidationError({'message':f'group_id {group_id} not found'})
            return Task.objects.create(owner=owner,group=group,**validated_data)    
        else :
            return Task.objects.create(owner=owner,**validated_data) 
      def update(self, instance, validated_data):
            owner  =self.context['request'].user
            group_id  =self.context['request'].data.get('group','')
            instance.owner = validated_data.get('owner', owner)
            if group_id =='':
                  instance.group = validated_data.get('group',None)
            else :
                  try:
                        global group
                        group =TaskGroup.objects.get(id=group_id)
                        if not group.owner == owner:
                              raise serializers.ValidationError({'message':f'you are not autherized to this group'},403)
                         
                  except TaskGroup.DoesNotExist:
                        raise serializers.ValidationError({'message':f'group_id {group_id} not found'})
                  instance.group =group
            instance.title = validated_data.get('title', instance.title)
            instance.description =validated_data.get('description',instance.description)
            instance.save()
            return instance
             
          