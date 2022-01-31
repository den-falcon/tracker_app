from django.db import models
from django.urls import reverse


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата создания')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse('project-view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.start_date}'

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проэкт'
        verbose_name_plural = 'Проэкты'


class Task(models.Model):
    summary = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('tracker_app.Status', related_name='Statuses', on_delete=models.PROTECT,
                               verbose_name='Статус')
    project = models.ForeignKey('tracker_app.Project', related_name='Tasks', on_delete=models.CASCADE,
                                verbose_name='Проэкт')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата обновления')
    type = models.ManyToManyField('tracker_app.Type', related_name='tasks', through='tracker_app.TaskType',
                                  through_fields=('task', 'type'))

    def get_absolute_url(self):
        return reverse('task-view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.summary} ({self.type.all()[0]}) {self.created_at}'

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


class TaskType(models.Model):
    task = models.ForeignKey('tracker_app.Task', related_name='task_types', on_delete=models.CASCADE,
                             verbose_name='Задача')
    type = models.ForeignKey('tracker_app.Type', related_name='type_tasks', on_delete=models.CASCADE,
                             verbose_name='Тип')

    def __str__(self):
        return f'{self.task} | {self.type}'

    class Meta:
        db_table = 'tasktypes'
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'


class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
