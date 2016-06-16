from . import views
from content import creation as content_creation, views as content_views
from django.conf import urls

urlpatterns = [
    urls.url(r'^gestalt/$', views.GestaltList.as_view(), name='gestalt-index'),
    urls.url(r'^gestalt/(?P<pk>[0-9]+)/edit/$', views.GestaltUpdate.as_view(), name='gestalt-update'),
    urls.url(r'^gestalt/(?P<pk>[0-9]+)/edit/avatar/$', views.GestaltAvatarUpdate.as_view(), name='gestalt-avatar-update'),
    urls.url(r'^gestalt/(?P<pk>[0-9]+)/edit/background/$', views.GestaltBackgroundUpdate.as_view(), name='gestalt-background-update'),
    urls.url(r'^gestalt/(?P<gestalt_pk>[0-9]+)/contact/$', content_creation.GestaltMessage.as_view(), name='gestalt-message-create'),
    urls.url(r'^group/$', views.GroupList.as_view(), name='group-index'),
    urls.url(r'^group/add/$', views.GroupCreate.as_view(), name='group-create'),
    urls.url(r'^group/attention/(?P<pk>[0-9]+)/delete/$', views.GroupAttentionDelete.as_view(), name='group-attention-delete'),
    urls.url(r'^group/membership/(?P<pk>[0-9]+)/delete/$', views.MembershipDelete.as_view(), name='membership-delete'),
    urls.url(r'^group/(?P<pk>[0-9]+)/edit/$', views.GroupUpdate.as_view(), name='group-update'),
    urls.url(r'^group/(?P<pk>[0-9]+)/edit/avatar/$', views.GroupAvatarUpdate.as_view(), name='group-avatar-update'),
    urls.url(r'^group/(?P<pk>[0-9]+)/edit/logo/$', views.GroupLogoUpdate.as_view(), name='group-logo-update'),
    urls.url(r'^group/(?P<group_pk>[0-9]+)/join/$', views.MembershipCreate.as_view(), name='membership-create'),
    urls.url(r'^group/(?P<group_pk>[0-9]+)/contact/$', content_creation.GroupMessage.as_view(), name='message-create'),
    urls.url(r'^group/(?P<group_pk>[0-9]+)/members/$', views.MembershipList.as_view(), name='membership-list'),
    urls.url(r'^group/(?P<group_pk>[0-9]+)/pay_attention/$', views.GroupAttentionCreate.as_view(), name='group-attention-create'),
    urls.url(r'^imprint/$', views.Imprint.as_view(), name='imprint'),
]
