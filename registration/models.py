from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def avatar_custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/avatar_photo/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="Foto Perfil", upload_to=avatar_custom_upload_to, blank=True)
    bio = models.TextField(verbose_name="Biografía", null=True, blank=True)
    link = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    rut = models.CharField(verbose_name="Rut", max_length=11, null=True, blank=True, unique=True)
    birth_date = models.DateField(verbose_name="Fecha Nacimiento", null=True, blank=True)
    gender = models.CharField(verbose_name="Género", max_length=15, null=True, blank=True)
    marital_status = models.CharField(verbose_name="Estado Civil", max_length=20, null=True, blank=True)
    agreement = models.NullBooleanField(verbose_name="Acuerdo", null=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")