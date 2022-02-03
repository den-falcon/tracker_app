from django.db.models import Q
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.list import MultipleObjectMixin

from tracker_app.forms import ProjectForm, SearchForm
from tracker_app.models import Project, Task
from tracker_app.views.base import SearchView


class ProjectsView(SearchView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects-view.html"
    paginate_by = 3
    paginate_orphans = 0
    search_fields = ['name__icontains', 'description__icontains']


class ProjectView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = "project"
    template_name = 'projects/project-view.html'
    paginate_by = 2
    paginate_orphans = 0
    search_value = None
    form = None

    def get_context_data(self, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        tasks = self.object.Tasks.filter(Q(summary__icontains=self.search_value) |
                                         Q(description__icontains=self.search_value))
        context = super().get_context_data(object_list=tasks, **kwargs)
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


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/create.html"


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'tasks/update.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project-view", kwargs={"pk": self.object.pk})


class ProjectDelete(DeleteView):
    model = Project

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("projects-view")
