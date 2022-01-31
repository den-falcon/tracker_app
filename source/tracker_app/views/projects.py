from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.list import MultipleObjectMixin

from tracker_app.forms import SearchForm, ProjectForm
from tracker_app.models import Project


class ProjectsView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects-view.html"
    paginate_by = 3
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by("-start_date")

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


class ProjectView(DetailView, MultipleObjectMixin):
    template_name = 'projects/project-view.html'
    model = Project
    context_object_name = "project"
    paginate_by = 2
    paginate_orphans = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_value = None
        self.form = None

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
