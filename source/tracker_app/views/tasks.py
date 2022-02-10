from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from tracker_app.forms import TaskForm
from tracker_app.models import Task, Project
from tracker_app.views.base import SearchView


class TasksView(SearchView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks-view.html"
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ['summary__icontains', 'description__icontains']


class TaskView(DetailView):
    template_name = 'tasks/view.html'
    model = Task


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('tracker_app:task-view', pk=task.pk)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse("tracker_app:project-view", kwargs={"pk": self.object.project.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("tracker_app:project-view", kwargs={"pk": self.object.project.pk})
