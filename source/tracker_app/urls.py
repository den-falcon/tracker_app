from django.urls import path

from tracker_app.views.projects import ProjectsView, ProjectView
from tracker_app.views.tasks import IndexView, TaskView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects-index'),
    path('tasks/', IndexView.as_view(), name='tasks-index'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/<int:project_pk>/task/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('task/create/', CreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', UpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', DeleteView.as_view(), name='task-delete')
]
