from django.urls import path

from .views import IndexView, TaskView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='view'),
    path('task/create/', CreateView.as_view(), name='create'),
    path('task/update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('task/delete/<int:pk>/', DeleteView.as_view(), name='delete')
]
