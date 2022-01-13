from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

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
                                           type_id=int(task_type),
                                           status_id=int(status))
            return redirect('view', pk=new_task.pk)
        return render(request, 'create.html', {"form": form})

