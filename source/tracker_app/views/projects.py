from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin

from tracker_app.forms import ProjectForm, SearchForm, AddUsers
from tracker_app.models import Project
from tracker_app.views.base import SearchView


class ProjectsView(SearchView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects-view.html"
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ['name__icontains', 'description__icontains']


class ProjectView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = "project"
    template_name = 'projects/project-view.html'
    paginate_by = 5
    paginate_orphans = 0
    search_value = None
    form = None

    def get_context_data(self, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        tasks = self.object.tasks.filter(Q(name__icontains=self.search_value) |
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


class ProjectCreate(PermissionRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "projects/create.html"
    permission_required = 'tracker_app.add_project'

    def has_permission(self):
        return super().has_permission()


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'tasks/update.html'
    form_class = ProjectForm
    permission_required = 'tracker_app.change_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse("tracker_app:project-view", kwargs={"pk": self.object.pk})


class ProjectAddUsers(PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = AddUsers
    template_name = 'projects/add_users.html'
    permission_required = 'tracker_app.add_users'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse("tracker_app:project-view", kwargs={"pk": self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('tracker_app:projects-view')
    permission_required = 'tracker_app.delete_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()
