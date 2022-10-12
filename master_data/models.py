from django.db import models

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


class Education(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Majoring(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class WorkPosition(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class StatusPerkawinan(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

