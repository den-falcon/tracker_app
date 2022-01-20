from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView
from django.urls import reverse

# Create your views here.
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


class CreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            summary = request.POST.get('summary')
            description = request.POST.get('description')
            task_type = request.POST.get('type')
            status = request.POST.get('status')
            new_task = Task.objects.create(summary=summary, description=description,
                                           status_id=int(status))
            return redirect('view', pk=new_task.pk)
        return render(request, 'create.html', {"form": form})


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

    # def get_initial(self):
    #     initial = {}
    #     for key in 'title', 'content', 'author':
    #         initial[key] = getattr(self.article, key)
    #     initial['tags'] = self.article.tags.all()
    #     return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        # tags = form.cleaned_data.pop('tags')
        # for key, value in form.cleaned_data.items():
        #     if value is not None:
        #         setattr(self.article, key, value)
        # self.article.save()
        # self.article.tags.set(tags)
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


