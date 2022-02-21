from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy

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


class TaskCreate(PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    permission_required = 'tracker_app.add_task'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('tracker_app:task-view', pk=task.pk)


class TaskUpdate(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    form_class = TaskForm
    permission_required = 'tracker_app.change_task'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()

    def get_success_url(self):
        return reverse("tracker_app:project-view", kwargs={"pk": self.object.project.pk})


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tracker_app:projects-view')
    permission_required = 'tracker_app.delete_task'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().project.users.all()
