from django.urls import path

from grouprise.core.urls import api_router
from grouprise.features.groups.rest_api import GroupSet
from grouprise.features.groups.views import (
        Create, ImageUpdate, List, RecommendView, SubscriptionsMemberships, Update)

api_router.register(r'groups', GroupSet, 'group')

urlpatterns = [
    path('stadt/groups', List.as_view(), name='group-index'),
    path('stadt/groups/add', Create.as_view(), name='group-create'),
    path('stadt/settings/group', Update.as_view(), name='group-settings'),
    path('stadt/settings/group/images', ImageUpdate.as_view(), name='group-image-settings'),
    path(
        'stadt/settings/group/subscriptions-memberships', SubscriptionsMemberships.as_view(),
        name='subscriptions-memberships-settings'
    ),
    path('<slug:group>/actions/recommend', RecommendView.as_view(), name='recommend-group'),
]
