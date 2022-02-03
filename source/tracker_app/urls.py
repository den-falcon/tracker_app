from django.urls import path

from tracker_app.views.projects import ProjectsView, ProjectView, ProjectCreate
from tracker_app.views.tasks import TasksView, TaskView, TaskUpdate, TaskDeleteView, TaskCreate

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects-view'),
    path('tasks/', TasksView.as_view(), name='tasks-view'),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('task/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('project/<int:project_pk>/task/create/', TaskCreate.as_view(), name='task-create'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete')
]
