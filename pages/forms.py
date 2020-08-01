from django import forms
from .models import PageVideo, PageImage, Page


class PageVideoForm(forms.ModelForm):

    class Meta:
        model = PageVideo
        fields = ['name', 'tag', 'description', 'link']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Video', 'style': 'text-transform:none'}),
            'tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Tag Video', 'style': 'text-transform:none'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'style': 'text-transform:none'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace Video', 'style': 'text-transform:none'}),
        }
        labels = {
            'name':'',
            'tag':'',
            'description':'',
            'link':''
        }
    
    pages = forms.ModelMultipleChoiceField(queryset=Page.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['pages'] = [t.pk for t in 
                kwargs['instance'].page_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=False):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.page_set.clear()
            for page in self.cleaned_data['pages']:
                instance.page_set.add(page)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # if commit:
        instance.save()
        self.save_m2m()

        return instance


class PageImageForm(forms.ModelForm):

    class Meta:
        model = PageImage
        fields = ['name', 'tag', 'link', 'uploadlink']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre Imágen', 'style': 'text-transform:none'}),
            'tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Tag Imágen', 'style': 'text-transform:none'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace Imágen', 'style': 'text-transform:none'}),
            'uploadlink': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels = {
            'name':'',
            'tag':'',
            'link':'',
            'uploadlink':''
        }

    pages = forms.ModelMultipleChoiceField(queryset=Page.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['pages'] = [t.pk for t in 
                kwargs['instance'].page_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=False):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.page_set.clear()
            for page in self.cleaned_data['pages']:
                instance.page_set.add(page)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # if commit:
        instance.save()
        self.save_m2m()

        return instance


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'tag', 'summary', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Título Página', 'style': 'text-transform:none'}),
            'tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Tag Página', 'style': 'text-transform:none'}),
            'summary': forms.Textarea(attrs={'class':'form-control', 'style': 'text-transform:none'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'style': 'text-transform:none'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Orden Página'}),
        }
        labels = {
            'title':'',
            'tag':'',
            'summary':'',
            'content':'',
            'order':''
        }