from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile
from courses.models import Category, Course
import random

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario', 'style': 'text-transform:none'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email', 'style': 'text-transform:none'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña', 'style': 'text-transform:none'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la Contraseña', 'style': 'text-transform:none'})
        return form
    
    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        context['category_list'] = Category.objects.all()
        
        # Others Courses [Begin]
        if len(context['course_list']) < 3:
            context['saved_courses'] = context['course_list']
        else:
            # Random Courses [Begin]
            saved_numbers = []
            saved_numbers = random.sample(range(0,len(context['course_list'])), 3)
            saved_courses = []
            for number in saved_numbers:
                saved_courses.append(context['course_list'][number])
            context['saved_courses'] = saved_courses
            # Random Courses [Finish]
        # Others Courses [Finish]

        return context

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # recuperar objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        context['category_list'] = Category.objects.all()
        
        # Others Courses [Begin]
        if len(context['course_list']) < 3:
            context['saved_courses'] = context['course_list']
        else:
            # Random Courses [Begin]
            saved_numbers = []
            saved_numbers = random.sample(range(0,len(context['course_list'])), 3)
            saved_courses = []
            for number in saved_numbers:
                saved_courses.append(context['course_list'][number])
            context['saved_courses'] = saved_courses
            # Random Courses [Finish]
        # Others Courses [Finish]

        return context

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        # recuperar objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email', 'style': 'text-transform:none'})
        return form

    def get_context_data(self, **kwargs):
        context = super(EmailUpdate, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        context['category_list'] = Category.objects.all()
        
        # Others Courses [Begin]
        if len(context['course_list']) < 3:
            context['saved_courses'] = context['course_list']
        else:
            # Random Courses [Begin]
            saved_numbers = []
            saved_numbers = random.sample(range(0,len(context['course_list'])), 3)
            saved_courses = []
            for number in saved_numbers:
                saved_courses.append(context['course_list'][number])
            context['saved_courses'] = saved_courses
            # Random Courses [Finish]
        # Others Courses [Finish]

        return context