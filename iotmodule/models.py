from django.db import models
from registration.models import Profile

class Device(models.Model):
    alias = models.CharField(verbose_name="Alias del Dispositivo", max_length=200, null=False, blank=False)
    serial = models.CharField(verbose_name="Número Serial del Dispositivo", max_length=100, null=False, blank=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "dispositivo"
        verbose_name_plural = "dispositivos"
        ordering = ['id', 'alias']

    def __str__(self):
        return self.id