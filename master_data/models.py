from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _


class Zone(models.Model):
    ZONE_TYPE = (
        (1, 'Kabupaten'),
        (2, 'Kota'),
    )
    name = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField(choices=ZONE_TYPE)
    province = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zona'


class Education(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Pendidikan'
        verbose_name_plural = 'Pendidikan'


class Majoring(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Jurusan Pendidikan'
        verbose_name_plural = 'Jurusan Pendidikan'


class WorkPosition(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Posisi'
        verbose_name_plural = 'Posisi'


class StatusPerkawinan(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Status Perkawinan'
        verbose_name_plural = 'Status Perkawinan'


class Religion(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(_("Description"), null=True, blank=True)

    def __str__(self) -> str:
        try:
            return self.name
        except:
            return ''

    class Meta:
        verbose_name = 'Agama'
        verbose_name_plural = 'Agama'


class AdditionalQuestion(models.Model):
    text = models.TextField(_("Pertanyaan"))
    status = models.BooleanField(_("Status"), default=True)

    def __str__(self) -> str:
        try:
            return f"{self.text[:15]}..."
        except:
            return "-"

    class Meta:
        verbose_name = 'Pertanyaan Lainnya'
        verbose_name_plural = 'Pertanyaan Lainnya'
