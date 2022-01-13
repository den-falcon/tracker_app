from django.urls import path

from .views import IndexView, TaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='view')
]