from django.views import generic

from core.views import base
from features.associations import models as associations
from features.content import models as content


class List(base.PermissionMixin, generic.ListView):
    permission_required = 'articles.view_list'
    model = associations.Association
    template_name = 'articles/list.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(
                container_type=content.Content.get_content_type()
                ).can_view(self.request.user).order_by('-content__versions__time_created')
