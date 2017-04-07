from . import creation, views
from django.conf import urls


urlpatterns = [
    urls.url(
        r'^content/(?P<content_pk>[0-9]+)/image/$',
        views.ImageList.as_view(),
        name='content-image-list'),
    urls.url(
        r'^content/(?P<content_pk>[0-9]+)/image/add/$',
        creation.ImageCreate.as_view(),
        name='image-create'),
    urls.url(r'^event/add/$', creation.Event.as_view(), name='event-create'),
    urls.url(r'^event/(?P<pk>[0-9]+)/edit/$', views.EventUpdate.as_view(), name='event-update'),
    urls.url(
        r'^event/(?P<year>[0-9]{4})/(?P<month>[-\w]+)/(?P<day>[0-9]+)/$',
        views.EventDay.as_view(),
        name='event-day'),
    urls.url(r'^gallery/$', views.GalleryList.as_view(), name='gallery-index'),
    urls.url(r'^gallery/add/$', creation.Gallery.as_view(), name='gallery-create'),
    urls.url(r'^markdown/$', views.Markdown.as_view(), name='markdown'),
]
