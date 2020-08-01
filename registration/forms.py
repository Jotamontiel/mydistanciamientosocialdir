from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'rut', 'birth_date', 'gender', 'marital_status', 'agreement', 'user']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía', 'style': 'text-transform:none'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace', 'style': 'text-transform:none'}),
            'rut': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Rut', 'style': 'text-transform:none'}),
            'birth_date': forms.DateInput(attrs={'class':'form-control mt-3 date', 'placeholder':'DD/MM/AAAA', 'style': 'text-transform:none'}),
            'gender': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Género', 'style': 'text-transform:none'}),
            'marital_status': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Estado Civil', 'style': 'text-transform:none'}),
            'agreement': forms.NullBooleanSelect(attrs={'class':'form-control mt-3', 'placeholder':'Estado Acuerdo', 'style': 'text-transform:none', 'required': '2'}),
            'user': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Usuario', 'style': 'text-transform:none'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email