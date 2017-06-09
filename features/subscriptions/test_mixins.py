from . import filters, models
from entities import models as entities
from features.gestalten import tests as gestalten
from features.groups import tests as groups
from features.memberships import test_mixins as memberships


class GroupSubscribedMixin(gestalten.AuthenticatedMixin, groups.GroupMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        models.Subscription.objects.create(
                subscribed_to=cls.group, subscriber=cls.gestalt)


class OtherGroupSubscriberMixin(
        gestalten.OtherGestaltMixin, groups.GroupMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        models.Subscription.objects.create(
                subscribed_to=cls.group,
                subscriber=cls.other_gestalt)


class AllContentUnsubscribedMixin(memberships.MemberMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        s = models.Subscription.objects.create(
                subscribed_to=cls.group, subscriber=cls.gestalt, unsubscribe=True)
        models.Filter.objects.create(
                filter_id=filters.all_content.filter_id, subscription=s)


class ExternalUnsubscribedMixin(memberships.MemberMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        s = models.Subscription.objects.create(
                subscribed_to=cls.group, subscriber=cls.gestalt, unsubscribe=True)
        models.Filter.objects.create(
                filter_id=filters.initial_author_no_member.filter_id, subscription=s)


class NoNotificationToOtherGestalt:
    def test_associate_content(self):
        entities.GroupContent.objects.create(
                content=self.content, group=self.group)
        self.assertNoNotificationSent()


class NotificationToOtherGestalt:
    def test_associate_content(self):
        entities.GroupContent.objects.create(
                content=self.content, group=self.group)
        self.assertNotificationSent()
        self.assertNotificationRecipient(self.other_gestalt)


class SenderIsAnonymous:
    def test_sender_name(self):
        entities.GroupContent.objects.create(
                content=self.content, group=self.group)
        self.assertNotificationSenderAnonymous()


class SenderNameIsGestalt:
    def test_sender_name(self):
        entities.GroupContent.objects.create(
                content=self.content, group=self.group)
        self.assertNotificationSenderName(self.gestalt)
