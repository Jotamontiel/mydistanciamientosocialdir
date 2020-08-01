from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Ubicación (Opcional)", null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="Dirección de la Ubicación")
    image = models.ImageField(verbose_name="Imágen (Opcional)", upload_to="courses/location", null=True, blank=True)
    latitude = models.FloatField(verbose_name="Latitud (Opcional)", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Longitud (Opcional)", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "ubicación"
        verbose_name_plural = "ubicaciones"
        ordering = ['created']
    
    def __str__(self):
        return self.address


class Modality(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Modalidad")
    content = RichTextField(verbose_name="Descripción")
    state = models.CharField(max_length=100, verbose_name="Estado (Opcional)", null=True, blank=True)
    duration = models.CharField(max_length=100, verbose_name="Duración (Opcional)", null=True, blank=True)
    period = models.CharField(max_length=200, verbose_name="Periodo (Opcional)", null=True, blank=True)
    inscribed = models.IntegerField(verbose_name="Inscritos (Opcional)", null=True, blank=True)
    quotas = models.IntegerField(verbose_name="Cupos (Opcional)", null=True, blank=True)
    location = models.ManyToManyField(Location, verbose_name="Ubicaciones")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "modalidad"
        verbose_name_plural = "modalidades"
        ordering = ['created']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    content = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen (1920x1080 px)", upload_to="courses/category")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorias"
        ordering = ['created']
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nombre del Curso")
    initials = models.CharField(max_length=50, verbose_name="Sigla del Curso")
    shortcontent = RichTextField(max_length=250, verbose_name="Breve Descripción (Opcional)", null=True, blank=True)
    content = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imágen (940x567 px)", upload_to="courses/course")
    managers = models.CharField(max_length=300, verbose_name="Encargado(s)")
    modality = models.ManyToManyField(Modality, verbose_name="Modalidades")
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ['created']
    
    def __str__(self):
        return self.name