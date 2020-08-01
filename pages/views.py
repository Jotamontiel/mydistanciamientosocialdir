from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import PageVideo, PageImage, Page
from .forms import PageVideoForm, PageImageForm, PageForm
from courses.models import Category, Course
import random
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


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


@method_decorator(staff_member_required, name='dispatch')
class PageVideoListView(ListView):
    model = PageVideo
    template_name = 'pages/page_video_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PageVideoListView, self).get_context_data(**kwargs)
        
        #Recuperar id de la página para encontrar los videos asociados
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[3]
        context['pageid'] = page_id
        context['pagevideo_list'] = PageVideo.objects.filter(page=page_id)
        #context['pagevideo_list'] = page_selected.video.all()
        
        paginator = Paginator(list(context['pagevideo_list']), self.paginate_by)
        page_number = self.request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
        context['pagevideo_list'] = page_obj
        context['page_obj'] = page_obj

        return context


@method_decorator(staff_member_required, name='dispatch')
class PageImageListView(ListView):
    model = PageImage
    template_name = 'pages/page_image_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(PageImageListView, self).get_context_data(**kwargs)
        
        #Recuperar id de la página para encontrar las imágenes asociadas
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[3]
        context['pageid'] = page_id
        context['pageimage_list'] = PageImage.objects.filter(page=page_id)
        #context['pageimage_list'] = page_selected.image.all()

        paginator = Paginator(list(context['pageimage_list']), self.paginate_by)
        page_number = self.request.GET.get('page')
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.get_page(1)
        except EmptyPage:
            page_obj = paginator.get_page(paginator.num_pages)
        context['pageimage_list'] = page_obj
        context['page_obj'] = page_obj
        
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
class PageVideoCreate(CreateView):
    model = PageVideo
    form_class = PageVideoForm
    template_name = 'pages/page_video_form.html'
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageImageCreate(CreateView):
    model = PageImage
    form_class = PageImageForm
    template_name = 'pages/page_image_form.html'
    success_url = reverse_lazy('pages:pages')


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
class PageVideoUpdate(UpdateView):
    model = PageVideo
    form_class = PageVideoForm
    template_name = 'pages/page_video_update_form.html'

    def get_success_url(self):

        #Recuperar id de la página
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[4]
        return reverse_lazy('pages:video_update', args=[self.object.id,page_id]) + '?ok'
    
    def get_context_data(self, **kwargs):
        context = super(PageVideoUpdate, self).get_context_data(**kwargs)
        
        #Recuperar id de la página
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[4]
        context['page_selected'] = Page.objects.filter(id=page_id).first()
        return context


@method_decorator(staff_member_required, name='dispatch')
class PageImageUpdate(UpdateView):
    model = PageImage
    form_class = PageImageForm
    template_name = 'pages/page_image_update_form.html'

    def get_success_url(self):

        #Recuperar id de la página
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[4]
        return reverse_lazy('pages:image_update', args=[self.object.id,page_id]) + '?ok'
    
    def get_context_data(self, **kwargs):
        context = super(PageImageUpdate, self).get_context_data(**kwargs)
        
        #Recuperar id de la página
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[4]
        context['page_selected'] = Page.objects.filter(id=page_id).first()
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


@method_decorator(staff_member_required, name='dispatch')
class PageVideoDelete(DeleteView):
    model = PageVideo
    template_name = 'pages/page_video_confirm_delete.html'
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageImageDelete(DeleteView):
    model = PageImage
    template_name = 'pages/page_image_confirm_delete.html'
    success_url = reverse_lazy('pages:pages')


class NewspaperDisplayView(DetailView):
    model = Page
    template_name = "pages/newspaper_display.html"

    def get_context_data(self, **kwargs):
        context = super(NewspaperDisplayView, self).get_context_data(**kwargs)
        
        #Recuperar id de la página
        path_aux = self.request.path
        path_new = []
        path_new = path_aux.split("/")
        page_id = path_new[3]
        context['pageimage_list'] = PageImage.objects.filter(page=page_id)
        context['pagevideo_list'] = PageVideo.objects.filter(page=page_id)

        return context