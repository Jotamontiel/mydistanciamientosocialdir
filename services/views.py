from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Service, Associated
from courses.models import Category, Course
import random

# Create your views here.
class ServicesListView(ListView):
    model = Service
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        context['category_list'] = Category.objects.all()
        context['associated_list'] = Associated.objects.all()
        context['hidd'] = False
        if context['associated_list']:
            context['hidd'] = True
        else:
            context['hidd'] = False
        
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