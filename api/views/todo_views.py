from rest_framework import generics
from api.models import Todo
from api.serializers import todo_serializers

class CreateTodoViews(generics.CreateAPIView):
    """ Добавление задачи """

    serializer_class = todo_serializers.CreateTodoSerializer


class DeleteTodoViews(generics.DestroyAPIView):
    """ Удаление задачи по идентификации """

    queryset = Todo.objects.all()
    serializer_class = todo_serializers.DeleteTodoSerializer


class UpdateTodoViews(generics.UpdateAPIView):
    """ Обновления задачи по идентификации"""

    queryset = Todo.objects.all()
    serializer_class = todo_serializers.UpdateTodoSerializer


class GetTodoViews(generics.ListAPIView):
    """ Вывод всех задач"""

    queryset = Todo.objects.all()
    serializer_class = todo_serializers.GetTodoSerializers





