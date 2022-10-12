from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
from django.utils.functional import cached_property

from base.enums import UFChoices


class SoftDeleteQuerySet(models.query.QuerySet):
    def delete(self, cascade=None):
        cascade = True
        if cascade:  # delete one by one if cascade
            for obj in self.all():
                obj.delete(cascade=cascade)
        return self.update(is_deleted=True, deleted_at=now())

    def hard_delete(self):
        return super().delete()


class DeletedQuerySet(models.query.QuerySet):
    def restore(self, *args, **kwargs):
        qs = self.filter(*args, **kwargs)
        qs.update(is_deleted=False, deleted_at=None)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, self._db).filter(is_deleted=True)


class BaseManager(models.Manager):
    def get_owner_queryset(self, user):
        queryset = super().get_queryset()
        return queryset.filter(owner=user)

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, self._db).filter(is_deleted=False)


class GlobalManager(models.Manager):
    pass


class BaseLog(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding or self.created_at is None:
            self.created_at = now()
        self.updated_at = now()
        super().save(*args, **kwargs)


class BaseModel(BaseLog):
    objects = BaseManager()
    deleted_objects = DeletedManager()
    global_objects = GlobalManager()

    class Meta:
        abstract = True

    def delete(self, *args, cascade=None, **kwargs):
        cascade = True
        self.is_deleted = True
        self.deleted_at = now()
        self.save()
        self.after_delete()
        if cascade:
            self.delete_related_objects()

    def restore(self, cascade=None):
        cascade = True
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        self.after_restore()
        if cascade:
            self.restore_related_objects()

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


class BaseAddressBR(BaseModel):
    cep = models.CharField(
        verbose_name=_("CEP"), max_length=9, blank=True, null=True
    )
    logradouro = models.TextField(
        verbose_name=_("Logradouro"), blank=True, null=True
    )
    numero = models.CharField(
        verbose_name=_("Número"), max_length=128, blank=True, null=True
    )
    bairro = models.CharField(
        verbose_name=_("Bairro"), max_length=255, blank=True, null=True
    )
    localidade = models.CharField(
        verbose_name=_("Cidade"), max_length=255, blank=True, null=True
    )
    uf = models.CharField(
        verbose_name=_("UF"), max_length=2, choices=UFChoices.choices, blank=True, null=True
    )
    inscricao_estadual = models.CharField(
        verbose_name=_("Inscrição Estadual"), max_length=55, blank=True, null=True
    )
    inscricao_municipal = models.CharField(
        verbose_name=_("Inscrição Municipal"), max_length=55, blank=True, null=True
    )
    codigo_municipio = models.CharField(
        verbose_name=_("Código Município"), max_length=55, blank=True, null=True
    )
    complemento = models.TextField(
        verbose_name=_("Complemento"), blank=True, null=True
    )
    observacao = models.TextField(
        verbose_name=_("Observação"), blank=True, null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        full_address = self.full_address
        if not full_address:
            return _("Fake model test {}").format(self.id)
        return full_address

    @cached_property
    def full_address(self):
        full_address = ""
        if self.logradouro:
            full_address += self.logradouro
        if self.numero:
            full_address += f", {self.numero}"
        if self.bairro:
            full_address += f", {self.bairro}"
        if self.localidade:
            full_address += f", {self.localidade}"
        if self.uf:
            full_address += f" - {self.uf}"
        if self.complemento:
            full_address += f" ({self.complemento})"
        return full_address

    def get_data_as_dict(self):
        return {
            'cep': self.cep,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'localidade': self.localidade,
            'uf': self.uf,
            'inscricao_estadual': self.inscricao_estadual,
            'inscricao_municipal': self.inscricao_municipal,
            'codigo_municipio': self.codigo_municipio,
            'complemento': self.complemento,
            'observacao': self.observacao
        }


class FakeModelTest(BaseAddressBR):

    class Meta:
        verbose_name = _("Fake model test")
        verbose_name_plural = _("Fake model tests")
