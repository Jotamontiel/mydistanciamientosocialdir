from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['alias', 'serial']
        widgets = {
            'alias': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Alias del Dispositivo', 'style': 'text-transform:none'}),
            'serial': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Número de Serie del Dispositivo', 'style': 'text-transform:none'}),
        }
