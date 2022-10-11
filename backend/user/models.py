from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _
from django.utils.timezone import now

from base.models import BaseLog, BaseManager, DeletedManager, GlobalManager


class CustomUserBaseManager(UserManager, BaseManager):
    pass


class CustomUserDeletedManager(UserManager, DeletedManager):
    pass


class CustomUserGlobalManager(UserManager, GlobalManager):
    pass


class CustomUser(AbstractUser, BaseLog):
    objects = CustomUserBaseManager()
    deleted_objects = CustomUserDeletedManager()
    global_objects = CustomUserGlobalManager()

    def delete(self, cascade=None, *args, **kwargs):
        cascade = True
        self.is_deleted = True
        self.deleted_at = now()
        self.save()
        self.after_delete()
        if cascade:
            self.delete_related_objects()
        # TODO: Call soft_delete_signals

    def restore(self, cascade=None):
        cascade = True
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        self.after_restore()
        if cascade:
            self.restore_related_objects()
        # TODO: Call soft_delete_signals

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def get_related_objects(self):
        return []

    def delete_related_objects(self):
        for obj in self.get_related_objects():
            obj.delete()

    def restore_related_objects(self):
        for obj in self.get_related_objects():
            obj.restore()

    def after_delete(self):
        pass

    def after_restore(self):
        pass
