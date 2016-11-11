from django.contrib.contenttypes import fields as contenttypes
from django.db import models


class Association(models.Model):
    container = contenttypes.GenericForeignKey('container_type', 'container_id')
    container_id = models.PositiveIntegerField()
    container_type = models.ForeignKey(
            'contenttypes.ContentType', related_name='container_associations')

    entity = contenttypes.GenericForeignKey('entity_type', 'entity_id')
    entity_id = models.PositiveIntegerField()
    entity_type = models.ForeignKey(
            'contenttypes.ContentType', related_name='entity_associations')
