from django import shortcuts
from django.contrib.messages import views as messages
from django import urls
from django.shortcuts import get_object_or_404
from django.views import generic

import core.views
import features.contributions.forms
import features.contributions.view_mixins
from features.gestalten.models import Gestalt
from features.associations import models as associations
from features.groups import models as groups
from features.groups.models import Group
from . import forms


class Conversation(
        features.contributions.view_mixins.ContributionFormMixin,
        core.views.PermissionMixin,
        generic.DetailView):

    permission_required = 'conversations.view'
    permission_required_post = 'conversations.reply'
    model = associations.Association
    pk_url_kwarg = 'association_pk'
    template_name = 'conversations/detail.html'

    form_class = features.contributions.forms.Text


class Conversations(core.views.PermissionMixin, generic.ListView):
    model = associations.Association
    permission_required = 'conversations.list'
    template_name = 'conversations/list.html'
    paginate_by = 10

    def get_content(self):
        return associations.Association.objects.can_view(self.request.user)

    def get_queryset(self):
        return super().get_queryset().ordered_user_conversations(self.request.user)


class GroupConversations(Conversations):
    permission_required = 'conversations.list_group'
    template_name = 'conversations/list_group.html'

    def get_permission_object(self):
        self.group = shortcuts.get_object_or_404(groups.Group, pk=self.kwargs['group_pk'])
        return self.group

    def get_queryset(self):
        return super().get_queryset().filter_group_containers().filter(entity_id=self.group.id)


class CreateConversation(
        core.views.PermissionMixin, messages.SuccessMessageMixin, generic.CreateView):
    model = associations.Association
    template_name = 'conversations/create.html'

    form_class = forms.Create

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['has_author'] = self.request.user.is_authenticated
        kwargs['instance'] = associations.Association(entity=self.entity)
        kwargs['contribution'] = features.contributions.models.Contribution()
        if kwargs['has_author']:
            kwargs['contribution'].author = self.request.user.gestalt
        return kwargs

    def get_success_message(self, cleaned_data):
        if not self.request.user.is_authenticated:
            return 'Die Nachricht wurde versendet.'

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return urls.reverse('conversation', args=[self.object.pk])
        else:
            return self.entity.get_absolute_url()


class CreateGestaltConversation(CreateConversation):
    permission_required = 'conversations.create_gestalt_conversation'

    def get_permission_object(self):
        if not hasattr(self, 'entity'):
            self.entity = get_object_or_404(Gestalt, pk=self.kwargs['gestalt_pk'])
        return self.entity


class CreateGroupConversation(CreateConversation):
    permission_required = 'conversations.create_group_conversation'

    def get_permission_object(self):
        if not hasattr(self, 'entity'):
            self.entity = get_object_or_404(Group, pk=self.kwargs['group_pk'])
        return self.entity


class CreateAbuseConversation(CreateGroupConversation):
    def get(self, *args, **kwargs):
        kwargs['group_pk'] = Group.objects.operator_group().pk
        return super().get(*args, **kwargs)

    def get_initial(self):
        return {
                'subject': 'Missbrauch melden',
                'text': '{}\n\nIch bin der Ansicht, dass der Inhalt dieser Seite gegen '
                        'Regeln verstößt.'.format(
                            self.request.build_absolute_uri(self.kwargs['path']))}

    def get_object(self):
        self.kwargs['group_pk'] = Group.objects.operator_group().pk
        return super().get_object()
