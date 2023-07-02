from django.contrib import admin

from .models import FakeModelTest, AddressBR, Historic


class SoftDeletedModelAdmin(admin.ModelAdmin):
    list_filter = ("is_deleted", )
    list_display = ("__str__", "is_deleted")
    readonly_fields = ("created_at", "updated_at", "deleted_at", "is_deleted",)


class FakeModelTestAdmin(SoftDeletedModelAdmin):
    pass


class AddressBRAdmin(SoftDeletedModelAdmin):
    pass


class HistoricAdmin(SoftDeletedModelAdmin):
    list_display = ("__str__", )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(FakeModelTest, FakeModelTestAdmin)
admin.site.register(AddressBR, AddressBRAdmin)
admin.site.register(Historic, HistoricAdmin)
