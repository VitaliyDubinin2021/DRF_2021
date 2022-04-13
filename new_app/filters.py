from django_filters import rest_framework as filters, DateFromToRangeFilter

from new_app.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(filters.FilterSet):
    project__name = filters.CharFilter(lookup_expr='contains')
    author__username = filters.CharFilter(lookup_expr='contains')
    created_at = DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['project__name', 'project', 'author__username', 'created_at']

