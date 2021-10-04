from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from todoist_api.models import BaseModel




class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class Todo(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, default='todo_name')
    todo_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    def __str__(self):
        return self.name