from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm
from courses.models import Category, Course
import random

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
    model = Page
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
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

class PageDetailView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
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

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

    def get_context_data(self, **kwargs):
        context = super(PageCreate, self).get_context_data(**kwargs)
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

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

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

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

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