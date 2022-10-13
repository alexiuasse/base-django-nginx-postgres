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

    def test_auto_create(self):
        obj = FakeModelTest.objects.create()
        obj.test = "B"
        obj.save()
        self.assertEqual(1, obj.historics.count())

    def test_fk(self):
        obj = FakeModelTest.objects.create()
        obj2 = FakeModelTest.objects.create()
        obj.test_fk = obj2
        obj.save()
        self.assertEqual(
            f"test_fk_id None -> {obj2.pk}",
            obj.historics.first().description
        )


class TestAddress(TestCase):
    def test_create(self):
        AddressBR.objects.create(
            content_object=FakeModelTest.objects.create(),
            cep="88047-595"
        )
        self.assertEqual(1, AddressBR.objects.all().count())
