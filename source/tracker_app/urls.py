from django.urls import path
from django.views.generic import RedirectView

from tracker_app.views.projects import (ProjectsView, ProjectView, ProjectCreate, ProjectUpdate, ProjectDelete,
                                        ProjectAddUsers)
from tracker_app.views.tasks import TasksView, TaskView, TaskUpdate, TaskDeleteView, TaskCreate

app_name = 'tracker_app'

urlpatterns = [
    path('', ProjectsView.as_view(), name='projects-view'),
    path('projects/', RedirectView.as_view(pattern_name="projects-view")),
    path('project/<int:pk>', ProjectView.as_view(), name='project-view'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project-delete'),
    path('tasks/', TasksView.as_view(), name='tasks-view'),
    path('task/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('project/<int:project_pk>/task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('project/<int:pk>/add_users', ProjectAddUsers.as_view(), name='add-users'),
]
