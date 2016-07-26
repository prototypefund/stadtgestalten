from . import models
from utils import tests


class MemberMixin(tests.AuthenticatedMixin, tests.GroupMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        models.Membership.objects.create(
                group=cls.group, member=cls.gestalt)