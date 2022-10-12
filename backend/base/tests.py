from django.test import TestCase

from .models import AddressBR, FakeModelTest, Historic


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


class TestHistoric(TestCase):
    def test_create(self):
        Historic.objects.create(
            content_object=FakeModelTest.objects.create(),
            description="Testing creation"
        )
        self.assertEqual(1, Historic.objects.all().count())


class TestAddress(TestCase):
    def test_create(self):
        AddressBR.objects.create(
            content_object=FakeModelTest.objects.create(),
            cep="88047-595"
        )
        self.assertEqual(1, AddressBR.objects.all().count())
