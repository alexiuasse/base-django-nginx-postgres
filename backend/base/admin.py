from django.contrib import admin

from .models import FakeModelTest, AddressBR, Historic


class SoftDeletedModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = self.model.deleted_objects.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


class FakeModelTestAdmin(SoftDeletedModelAdmin):
    pass


class AddressBRAdmin(SoftDeletedModelAdmin):
    pass


class HistoricAdmin(SoftDeletedModelAdmin):
    pass


# admin.site.register(FakeModelTest, FakeModelTestAdmin)
admin.site.register(FakeModelTest)
admin.site.register(AddressBR, AddressBRAdmin)
admin.site.register(Historic, HistoricAdmin)
