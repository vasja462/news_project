from django.db import models
from profiles.models import User

class Comments(models.Model):
    name_author = models.CharField(max_length=75,  default=None, null=True, verbose_name="Имя автора")
    text_comment = models.TextField(null=True, verbose_name="Новость")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name_author


class Label(models.Model):
    name = models.CharField(max_length=75,  default=None, null=True, verbose_name="Тег")

    def __str__(self):
        return self.name


class News(models.Model):
    CATEGORY = (
        ('Power', 'Власть'),
        ('Economy', 'Экономика'),
        ('regions', 'В регионах'),
        ('world', 'В мире'),
        ('Incidents', 'Происшествия'),
        ('Society', 'Общество'),
        ('Sport', 'Спорт'),
        ('culture', 'Культура'),
       )

    name = models.CharField(max_length=250,  default=None, null=True, verbose_name="Новость")
    description = models.TextField(null=True, verbose_name="Новость")
    created_at = models.DateTimeField(verbose_name="Дата создания")
    updated_at = models.DateTimeField(verbose_name="Дата изменения")
    activate = models.BooleanField(verbose_name="Опубликовано")
    comments = models.ForeignKey(Comments, on_delete=models.PROTECT, verbose_name="Автор")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    category = models.CharField(max_length=10,  choices=CATEGORY, default=None,
                                null=True, verbose_name="Катерогия")
    label = models.ManyToManyField(Label, verbose_name="Теги")

    def __str__(self):
        return self.name
