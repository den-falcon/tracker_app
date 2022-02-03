from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin

from tracker_app.forms import ProjectForm
from tracker_app.models import Project
from tracker_app.views.base import SearchView


class ProjectsView(SearchView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects-view.html"
    paginate_by = 3
    paginate_orphans = 0
    search_fields = ['name__icontains', 'description__icontains']


class ProjectView(SearchView, SingleObjectMixin):
    template_name = 'projects/project-view.html'
    model = Project
    context_object_name = "project"
    paginate_by = 2
    paginate_orphans = 0
    search_fields = ['summary__icontains', 'description__icontains']
    object = None

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object = self.get_object()
        tasks = self.object.Tasks.filter(self.get_query())
        context = super().get_context_data(object_list=tasks, **kwargs)
        context['object'] = self.object
        return context


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/create.html"
