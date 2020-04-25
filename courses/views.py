from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Course, Category, Modality, Location
import random

# Create your views here.
class CoursesListView(ListView):
    model = Course
    template_name = "courses/courses.html"
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
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

        # Selected Category [Begin]
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        if path_new[2]:
            context['idcategoryaux'] = int(path_new[2])
        else:
            context['idcategoryaux'] = ''
        # Selected Category [Finish]

        # Flag More Categories [Begin]
        if len(context['course_list']) > 1:
            context['numberCoursesFlag'] = True
        else:
            context['numberCoursesFlag'] = False
        # Flag More Categories [Finish]

        return context

class CoursesDetailView(DetailView):
    model = Course
    template_name = "courses/courses_detail.html"
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        context['category_list'] = Category.objects.all()
        context['modality_list'] = Modality.objects.all()
        context['location_list'] = Location.objects.all()
        context['hidd'] = False
        for aux_course in context['course_list']:
            if aux_course.pk != self.object.pk and aux_course.category == self.object.category:
                context['hidd'] = True

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