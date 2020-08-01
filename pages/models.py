from django.db import models
from ckeditor.fields import RichTextField


class PageVideo(models.Model):
    name = models.CharField(verbose_name="Nombre Video", max_length=200, null=False, blank=False)
    tag = models.CharField(verbose_name="Tag Video (Opcional)", max_length=100, null=True, blank=True)
    description = RichTextField(verbose_name="Descripción Video (Opcional)", null=True, blank=True)
    link = models.URLField(verbose_name="Enlace Video", max_length=600, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
        
    class Meta:
        verbose_name = "video de página"
        verbose_name_plural = "videos de página"
        ordering = ['tag', 'name']

    def __str__(self):
        return self.name


def avatar_custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/avatar_photo/' + filename


class PageImage(models.Model):
    name = models.CharField(verbose_name="Nombre Imágen", max_length=200, null=False, blank=False)
    tag = models.CharField(verbose_name="Tag Imágen (Opcional)", max_length=100, null=True, blank=True)
    link = models.URLField(verbose_name="Enlace Imágen (Opcional)", max_length=600, null=True, blank=True)
    uploadlink = models.ImageField(verbose_name="Subir Imágen (1920x1080 px, Opcional)", upload_to="pages/page", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "imágen de página"
        verbose_name_plural = "imágenes de página"
        ordering = ['tag', 'name']

    def __str__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(verbose_name="Título Página", max_length=200, null=False, blank=False)
    tag = models.CharField(verbose_name="Tag Página (Opcional)", max_length=100, null=True, blank=True)
    summary = RichTextField(verbose_name="Resumen Página (Opcional)", null=True, blank=True)
    content = RichTextField(verbose_name="Contenido Página (Opcional)", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden Página (Opcional)", default=0)
    video = models.ManyToManyField(PageVideo, verbose_name="Videos Página (Opcional)")
    image = models.ManyToManyField(PageImage, verbose_name="Imágenes Página (Opcional)")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title