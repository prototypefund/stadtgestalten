from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.views import generic
from django_filters import views as filters_views
from entities import filters
from features.memberships.rules import is_member_of
from content import models as content_models, views as content_views
from utils import views as utils_views
from core import fields, views
from core.views import base
from . import forms, models


class Mixin:
    def get_context_data(self, **kwargs):
        kwargs['group'] = self.get_group()
        return super().get_context_data(**kwargs)

    def get_group(self):
        for attr in ('object', 'related_object'):
            if hasattr(self, attr):
                instance = getattr(self, attr)
                if isinstance(instance, models.Group):
                    return instance
                if hasattr(instance, 'group'):
                    return instance.group
                if hasattr(instance, 'groups'):
                    return instance.groups.first()
        try:
            if 'group_pk' in self.kwargs:
                return models.Group.objects.get(
                        pk=self.kwargs['group_pk'])
            if 'group_slug' in self.kwargs:
                return models.Group.objects.get(
                        slug=self.kwargs['group_slug'])
            if 'group' in self.request.GET:
                return models.Group.objects.get(
                        slug=self.request.GET['group'])
            if 'content_pk' in self.kwargs:
                return content_models.Content.objects.get(
                        pk=self.kwargs['content_pk']).groups.first()
        except (content_models.Content.DoesNotExist,
                models.Group.DoesNotExist):
            pass
        return None


class Create(views.Create):
    permission = 'groups.create_group'

    action = 'Gruppe anlegen'
    menu = 'group'
    parent = 'group-index'
    title = 'Neue Gruppe'

    model = models.Group

    data_field_classes = (
            fields.current_gestalt('gestalt_created', null=True),
            fields.model_field('name'))


class List(base.PermissionMixin, filters_views.FilterView):
    permission_required = 'groups.view_list'
    filterset_class = filters.Group
    paginate_by = 10

    def get_queryset(self):
        return models.Group.objects.order_by('-score')


class Update(base.PermissionMixin, generic.UpdateView):
    permission_required = 'groups.change_group'
    model = models.Group
    template_name = 'groups/update.html'

    form_class = forms.Update
