from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def avatar_custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/avatar_photo/' + filename

def love_photo_custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.upload_most_love_photo.delete()
    return 'profiles/love_photo/' + filename

def meme_photo_custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.upload_first_meme_photo.delete()
    return 'profiles/meme_photo/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Foto Perfil", upload_to=avatar_custom_upload_to, blank=True)
    bio = models.TextField(verbose_name="Biografía", null=True, blank=True)
    link = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    nickname = models.CharField(verbose_name="Apodo", max_length=50, null=True, blank=True)
    name = models.CharField(verbose_name="Nombre", max_length=50, null=True, blank=True)
    father_last_name = models.CharField(verbose_name="Apellido Paterno", max_length=50, null=True, blank=True)
    mother_last_name = models.CharField(verbose_name="Apellido Materno", max_length=50, null=True, blank=True)
    rut = models.CharField(verbose_name="Rut", max_length=11, null=True, blank=True, unique=True)
    birth_date = models.DateField(verbose_name="Fecha Nacimiento", null=True, blank=True)
    gender = models.CharField(verbose_name="Género", max_length=15, null=True, blank=True)
    marital_status = models.CharField(verbose_name="Estado Civil", max_length=20, null=True, blank=True)
    lat = models.FloatField(verbose_name="Latitud", null=True, blank=True)
    lng = models.FloatField(verbose_name="Longitud", null=True, blank=True)
    upload_most_love_photo = models.ImageField(verbose_name="Foto Tesoro", upload_to=love_photo_custom_upload_to, blank=True)
    upload_first_track_id = models.CharField(verbose_name="Canción Favorita", max_length=30, null=True, blank=True) # Example: 7j74lucZ59vqN67Ipe2ZcY
    upload_first_meme_photo = models.ImageField(verbose_name="Meme Favorito", upload_to=meme_photo_custom_upload_to, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")