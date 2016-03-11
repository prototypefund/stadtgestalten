from django.conf import settings, urls
from django.conf.urls import static, url
from django.contrib import admin
from django.views import generic

from content import views as content_views
from entities import views as entities_views


urlpatterns = [
    # index
    url(r'^$', content_views.ContentList.as_view(), name='index'),
    # stadt namespace
    url(r'^stadt/', urls.include('allauth.urls')),
    url(r'^stadt/admin/', admin.site.urls),
    url(r'^stadt/content/add/(?:group=(?P<group_slug>[\w-]+))?$', content_views.ContentCreate.as_view(), name='content-create'),
    url(r'^stadt/content/(?P<pk>[0-9]+)/edit/(?:group=(?P<group_slug>[\w-]+))?$', content_views.ContentUpdate.as_view(), name='content-update'),
    url(r'^stadt/event/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$', content_views.EventDay.as_view(), name='event-day'),
    url(r'^stadt/gestalt/(?P<pk>[0-9]+)/edit/$', entities_views.GestaltUpdate.as_view(), name='gestalt-update'),
    url(r'^stadt/group/membership/add/group=(?P<group_slug>[\w-]+)/$', entities_views.GroupMembershipCreate.as_view(), name='group-membership-create'),
    url(r'^stadt/group/membership/(?P<pk>[0-9]+)/delete/$', entities_views.GroupMembershipDelete.as_view(), name='group-membership-delete'),
    url(r'^stadt/group/new/$', entities_views.GroupCreate.as_view(), name='group-create'),
    url(r'^stadt/group/(?P<pk>[0-9]+)/edit/$', entities_views.GroupUpdate.as_view(), name='group-update'),
    url(r'^stadt/imprint/$', generic.TemplateView.as_view(template_name='imprint.html'), name='imprint'),
         # stadt/media
         # stadt/static
    # gestalt namespaces
    url(r'^gestalt/(?P<slug>[\w.@+-]+)/$', entities_views.Gestalt.as_view(), name='gestalt'),
    url(r'^gestalt/(?P<gestalt_slug>[\w.@+-]+)/(?P<slug>[\w-]+)/$', content_views.Content.as_view(), name='content'),
    # group namespaces
    url(r'^(?P<slug>[\w-]+)$', entities_views.Group.as_view(), name='group'),
    url(r'^(?P<group_slug>[\w-]+)/(?P<slug>[\w-]+)/$', content_views.Content.as_view(), name='group-content'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
