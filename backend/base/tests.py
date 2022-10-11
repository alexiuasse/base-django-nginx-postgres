from django.test import TestCase

from .models import FakeModelTest


class TestDeletion(TestCase):
    def setUp(self):
        self.fake_obj = FakeModelTest.objects.create()

    def test_delete(self):
        self.fake_obj.delete()
        self.assertEqual(0, FakeModelTest.objects.all().count())
        self.assertEqual(1, FakeModelTest.deleted_objects.all().count())

    def test_restore(self):
        self.fake_obj.delete()
        self.assertEqual(True, self.fake_obj.is_deleted)
        self.fake_obj.restore()
        self.assertEqual(1, FakeModelTest.objects.all().count())
        self.assertEqual(0, FakeModelTest.deleted_objects.all().count())
