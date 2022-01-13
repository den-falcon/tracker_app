from django.urls import path

from .views import IndexView, TaskView, CreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='view'),
    path('task/create/', CreateView.as_view(), name='create')
]