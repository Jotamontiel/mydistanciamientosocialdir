from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import CapsuleForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Capsule
from courses.models import Category, Course
from registration.models import Profile
import random

# Create your views here.
class CapsuleListView(ListView):
    model = Capsule
    paginate_by = 3
    
class CapsuleDetailView(DetailView):
    model = Capsule

class CapsuleCreate(CreateView):
    model = Capsule
    form_class = CapsuleForm
    success_url = reverse_lazy('capsules:capsules')

    def get_context_data(self, **kwargs):
        context = super(CapsuleCreate, self).get_context_data(**kwargs)
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

    # Search for profile instance
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(id=self.request.user.id)
        return super(CapsuleCreate, self).form_valid(form)

class CapsuleUpdate(UpdateView):
    model = Capsule
    form_class = CapsuleForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('capsules:update', args=[self.object.id]) + '?ok'
    
    def get_context_data(self, **kwargs):
        context = super(PageUpdate, self).get_context_data(**kwargs)
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

class CapsuleDelete(DeleteView):
    model = Capsule
    success_url = reverse_lazy('capsules:capsules')

    def get_context_data(self, **kwargs):
        context = super(PageDelete, self).get_context_data(**kwargs)
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