from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^stadt/events/$',
        views.List.as_view(),
        name='events'),

    url(
        r'^stadt/events/add/$',
        views.Create.as_view(),
        name='create-event'),

    url(
        r'^stadt/events/export$',
        views.SiteCalendarExport.as_view(),
        name='export-site-events'),

    url(
        r'^stadt/events/public.ics$',
        views.SiteCalendarFeed(),
        name='site-events-feed'),

    url(
        r'^stadt/events/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',
        views.Day.as_view(),
        name='day-events'),

    url(
        r'^(?P<entity_slug>[\w.@+-]+)/events/add/$',
        views.Create.as_view(),
        name='create-group-event'),

    url(
        # TODO: remove 'gestalt/' prefix
        r'^gestalt/(?P<gestalt_slug>[\w.@+-]+)/events/(?P<domain>public|private).ics$',
        views.GestaltCalendarFeed(),
        name='gestalt-events-feed'),

    url(
        r'^(?P<group_slug>[\w-]+)/events/export$',
        views.GroupCalendarExport.as_view(),
        name='group-events-export'),

    url(
        r'^(?P<group_slug>[\w-]+)/events/(?P<domain>public|private).ics$',
        views.GroupCalendarFeed(),
        name='group-events-feed'),
]
