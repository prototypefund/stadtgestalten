import logging

import django.conf
import django.db.models.signals
import django_mailbox.signals
from django.dispatch import receiver

import core.models
from . import models, notifications

logger = logging.getLogger(__name__)


@receiver(django.db.models.signals.post_save, sender=models.Contribution)
def send_contribution_notification(sender, instance, created, **kwargs):
    if created:
        notifications.Contributed(instance=instance).send()


@receiver(django_mailbox.signals.message_received)
def process_incoming_message(sender, message, **args):
    token_beg = len(django.conf.settings.DEFAULT_REPLY_TO_EMAIL.split('{')[0])
    token_end = len(django.conf.settings.DEFAULT_REPLY_TO_EMAIL.rsplit('}')[1])
    token = message.to_addresses[0][token_beg:-token_end]
    try:
        try:
            in_reply_to_text = models.Contribution.objects.get_by_message_id(
                    message.get_email_object().get('In-Reply-To'))
        except models.Contribution.DoesNotExist:
            in_reply_to_text = None
        key = core.models.PermissionToken.objects.get(secret_key=token)
        text = models.Text.objects.create(text=message.text)
        models.Contribution.objects.create(
                author=key.gestalt,
                container=key.target.container,
                in_reply_to=in_reply_to_text,
                contribution=text)
    except core.models.PermissionToken.DoesNotExist:
        logger.error('Could not process message {}'.format(message.id))