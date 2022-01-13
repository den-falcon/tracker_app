from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    type = models.ForeignKey('tracker_app.Type', related_name='types', on_delete=models.PROTECT, verbose_name='Тип')
    status = models.ForeignKey('tracker_app.Status', related_name='Statuses', on_delete=models.PROTECT,
                               verbose_name='Статус')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.summary} ({self.type}) {self.created_at}'

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
