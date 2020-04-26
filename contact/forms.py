from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre', 'style':'text-transform:capitalize'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email, ej: XXXXXX@gmail.com', 'style':'text-transform:capitalize'}
    ), min_length=3, max_length=100)
    phone = forms.CharField(label="Teléfono", required=False, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu teléfono, ej: 09 XXXX XXXX'}
    ), min_length=3, max_length=1000)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':7, 'placeholder':'Escribe tu mensaje', 'style':'text-transform:lowercase'}
    ), min_length=3, max_length=1000)
