from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título Servicio", null=False, blank=False)
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo Servicio (Opcional)", null=True, blank=True)
    content = RichTextField(verbose_name="Contenido Servicio (Opcional)", null=True, blank=True)
    image1 = models.ImageField(verbose_name="Imágen 1 Servicio (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Imágen 2 Servicio (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    image3 = models.ImageField(verbose_name="Imágen 3 Servicio (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    link = models.URLField(max_length=400, verbose_name="Enlace Servicio (Opcional)", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['created']
    
    def __str__(self):
        return self.title


class Affiliated(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre Socio", null=False, blank=False)
    content = RichTextField(verbose_name="Descripción Socio (Opcional)", null=True, blank=True)
    logoimage = models.ImageField(verbose_name="Logo Socio (400x300 px)", upload_to="services/associated", blank=True)
    lat = models.FloatField(verbose_name="Latitud (Opcional)", null=True, blank=True)
    lon = models.FloatField(verbose_name="Longitud (Opcional)", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "socio"
        verbose_name_plural = "socios"
        ordering = ['created']
    
    def __str__(self):
        return self.name