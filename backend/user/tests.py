from django.test import TestCase

from .models import CustomUser


class TestUserDeletion(TestCase):
    def setUp(self):
        self.fake_obj = CustomUser.objects.create_user(
            'test',
            email="test@test.com",
            password="t3s123"
        )

    def test_delete(self):
        self.fake_obj.delete()
        self.assertEqual(0, CustomUser.objects.all().count())
        self.assertEqual(1, CustomUser.deleted_objects.all().count())

    def test_restore(self):
        self.assertEqual(True, self.fake_obj.is_deleted)
        self.fake_obj.restore()
        self.assertEqual(1, CustomUser.objects.all().count())
        self.assertEqual(0, CustomUser.deleted_objects.all().count())
