from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView
from django.urls import reverse

from .forms import TaskForm
from .models import Task


class IndexView(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)


class TaskView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)


class CreateView(FormView):
    form_class = TaskForm
    template_name = "create.html"
    object = None

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={"pk": self.object.pk})


class UpdateView(FormView):
    form_class = TaskForm
    template_name = "update.html"

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
        return reverse('view', kwargs={"pk": self.task.pk})

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get("pk"))


def article_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        kwargs['task'] = task
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect("index")


