from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image1 = models.ImageField(verbose_name="Imágen 1 (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Imágen 2 (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    image3 = models.ImageField(verbose_name="Imágen 3 (1200x658 px, Opcional)", upload_to="services/service", null=True, blank=True)
    link = models.URLField(max_length=400, verbose_name="Enlace (Opcional)", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['created']
    
    def __str__(self):
        return self.title


class Associated(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = RichTextField(verbose_name="Descripción (Opcional)", null=True, blank=True)
    logo = models.ImageField(verbose_name="Logo (400x300 px)", upload_to="services/associated")
    latitude = models.FloatField(verbose_name="Latitud (Opcional)", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Longitud (Opcional)", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "asociado"
        verbose_name_plural = "asociados"
        ordering = ['created']
    
    def __str__(self):
        return self.title