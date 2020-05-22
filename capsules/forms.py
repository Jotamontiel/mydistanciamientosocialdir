from django import forms
from .models import Capsule

class CapsuleForm(forms.ModelForm):
    class Meta:
        model = Capsule
        fields = ['name', 'father_last_name', 'mother_last_name', 'nickname', 'lat', 'lng', 'upload_most_love_photo', 'upload_first_track_id', 'upload_first_meme_photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Nombre', 'style': 'text-transform:none'}),
            'father_last_name': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apellido Paterno', 'style': 'text-transform:none'}),
            'mother_last_name': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apellido Materno', 'style': 'text-transform:none'}),
            'nickname': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Apodo', 'style': 'text-transform:none'}),
            'lat': forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Latitud', 'style': 'text-transform:none'}),
            'lng': forms.NumberInput(attrs={'class':'form-control mt-3', 'placeholder':'Longitud', 'style': 'text-transform:none'}),
            'upload_most_love_photo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'upload_first_track_id': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Canción Favorita', 'style': 'text-transform:none'}),
            'upload_first_meme_photo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
