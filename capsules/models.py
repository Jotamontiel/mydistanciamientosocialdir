from django.db import models
from registration.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

def love_photo_custom_upload_to(instance, filename):
    old_instance = Capsule.objects.get(pk=instance.pk)
    old_instance.upload_most_love_photo.delete()
    return 'capsules/love_photo/' + filename

def meme_photo_custom_upload_to(instance, filename):
    old_instance = Capsule.objects.get(pk=instance.pk)
    old_instance.upload_first_meme_photo.delete()
    return 'capsules/meme_photo/' + filename

class Capsule(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True,)
    name = models.CharField(verbose_name="Nombre", max_length=50, null=True, blank=True)
    father_last_name = models.CharField(verbose_name="Apellido Paterno", max_length=50, null=True, blank=True)
    mother_last_name = models.CharField(verbose_name="Apellido Materno", max_length=50, null=True, blank=True)
    nickname = models.CharField(verbose_name="Apodo", max_length=50, null=True, blank=True)
    lat = models.FloatField(verbose_name="Latitud", null=True, blank=True)
    lng = models.FloatField(verbose_name="Longitud", null=True, blank=True)
    upload_most_love_photo = models.ImageField(verbose_name="Foto Tesoro", upload_to=love_photo_custom_upload_to, blank=True)
    upload_first_track_id = models.CharField(verbose_name="Canción Favorita", max_length=30, null=True, blank=True) # Example: 7j74lucZ59vqN67Ipe2ZcY
    upload_first_meme_photo = models.ImageField(verbose_name="Meme Favorito", upload_to=meme_photo_custom_upload_to, blank=True)

    # class Meta:
    #     ordering = ['user__username']

# @receiver(post_save, sender=Profile)
# def ensure_capsule_exists(sender, instance, **kwargs):
#     if kwargs.get('created', False):
#         Capsule.objects.get_or_create(profile=instance)
#         print("Se acaba de crear una perfil y su cápsula enlazada")