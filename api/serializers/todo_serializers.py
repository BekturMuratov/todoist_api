from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from api.models import Todo


class CreateTodoSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =[
            'id',
            'name',
            'todo_category',
        ]

class DeleteTodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = [
            'id',
            'name',
            'todo_category',
        ]

class UpdateTodoSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class GetTodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'name',
            'todo_category',
        ]