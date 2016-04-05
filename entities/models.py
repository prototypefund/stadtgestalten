from . import querysets
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core import urlresolvers
from django.db import models

class Attention(models.Model):
    content = models.ForeignKey('content.Content', null=True, blank=True)
    gestalt = models.ForeignKey('Gestalt')
    group = models.ForeignKey('Group', null=True, blank=True)
    stadtgestalten = models.BooleanField()

class Gestalt(models.Model):
    about = models.TextField('Selbstauskunft', blank=True)
    avatar = models.ImageField(default=staticfiles_storage.url('avatar.png'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    
    def __str__(self):
        name = ' '.join(filter(None, [self.user.first_name, self.user.last_name]))
        return name if name else self.user.username

    def get_absolute_url(self):
        return urlresolvers.reverse('gestalt', args=[type(self).objects.get(pk=self.pk).user.username])

class GestaltContent(models.Model):
    content = models.OneToOneField('content.Content')
    gestalt = models.ForeignKey('Gestalt')

class Group(models.Model):
    address = models.TextField('Anschrift', blank=True)
    avatar = models.ImageField(default=staticfiles_storage.url('avatar.png'))
    content = models.ManyToManyField('content.Content', related_name='groups', through='GroupContent')
    date_created = models.DateField(auto_now_add=True)
    date_founded = models.DateField('Gruppe gegründet', null=True, blank=True)
    logo = models.ImageField(blank=True)
    members = models.ManyToManyField('Gestalt', through='Membership')
    name = models.CharField('Name', max_length=255)
    slug = models.SlugField('Adresse der Gruppenseite', unique=True)
    url = models.URLField('Adresse im Web', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return urlresolvers.reverse('group', args=[type(self).objects.get(pk=self.pk).slug])

class GroupContent(models.Model):
    content = models.OneToOneField('content.Content')
    group = models.ForeignKey('Group')
    pinned = models.BooleanField(default=False)

class Membership(models.Model):
    date_joined = models.DateField(auto_now_add=True)
    gestalt = models.ForeignKey('Gestalt')
    group = models.ForeignKey('Group')

    class Meta:
        unique_together = ('gestalt', 'group')
