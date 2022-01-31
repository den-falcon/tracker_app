from django.urls import path

from tracker_app.views.projects import ProjectsView, ProjectView, ProjectCreate
from tracker_app.views.tasks import IndexView, TaskView, UpdateView, DeleteView, TaskCreate

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects-view'),
    path('tasks/', IndexView.as_view(), name='tasks-index'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/<int:project_pk>/task/<int:task_pk>/', TaskView.as_view(), name='task-view'),
    path('project/<int:project_pk>/task/create/', TaskCreate.as_view(), name='task-create'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('task/update/<int:pk>/', UpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', DeleteView.as_view(), name='task-delete')
]
