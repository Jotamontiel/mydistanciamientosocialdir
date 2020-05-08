from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from courses.models import Category, Course
import random

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
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

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
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
