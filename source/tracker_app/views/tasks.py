from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.urls import reverse

from tracker_app.forms import TaskForm, SearchForm
from tracker_app.models import Task, Project


class IndexView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks-view.html"
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            print(self.search_value)
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by("-updated_at")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class TaskView(TemplateView):
    template_name = 'tasks/view.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('task_pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('task-view', project_pk=project.pk, task_pk=task.pk)


class UpdateView(FormView):
    form_class = TaskForm
    template_name = "tasks/update.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-view', kwargs={"task_pk": self.task.pk, 'project_pk': self.task.project.pk})

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))


class DeleteView(TemplateView):
    template_name = 'tasks/delete.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        pk = task.project.pk
        task.delete()
        return redirect("project-view", pk=pk)
