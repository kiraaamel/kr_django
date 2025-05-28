from django.db import models
from django.contrib.auth.models import User

class kmexam(models.Model):
    title = models.CharField("Название экзамена", max_length=255)
    created_at = models.DateTimeField("Дата создания записи", auto_now_add=True)
    exam_date = models.DateField("Дата проведения экзамена")
    image = models.ImageField("Задание по экзамену в виде картинки", upload_to='exam_images/')
    users = models.ManyToManyField(User, related_name='exams', verbose_name="Пользователи, который пишут экзамен")
    is_public = models.BooleanField("Опубликовано", default=False)

    def __str__(self):
        return self.title

