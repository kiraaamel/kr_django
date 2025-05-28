from django.contrib import admin
from django.contrib.auth.models import User
from .models import kmexam

@admin.register(kmexam)
class kmexamAdmin(admin.ModelAdmin):
    #поиск по названию экзамена и почте пользователя
    search_fields = ['title', 'users__email']
    #поиск по дате экзамена
    date_hierarchy = 'exam_date'
    # редактирование поля M2M
    filter_horizontal = ('users',)
    #фильтр по полю is_public и дате добавления записи
    list_filter = ['is_public', 'created_at']


    list_display = ['title', 'exam_date', 'is_public', 'created_at']
