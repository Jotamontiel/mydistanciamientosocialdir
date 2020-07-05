from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from courses.models import Category, Course
from registration.models import Profile
from capsules.models import Capsule
import random
import folium
from IPython.display import IFrame, HTML, display

class HomePageView(ListView):
    model = Category
    template_name = "core/home.html"
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()
        #context['capsule_list'] = Capsule.objects.all()

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
        if path_new[1]:
            context['idcategoryaux'] = int(path_new[2])
        else:
            context['idcategoryaux'] = ''
        # Selected Category [Finish]

        # Number Categories Calculation [Begin]
        categories_amount = len(context['category_list'])
        # Number Categories Calculation [Finish]

        # FlagSection [Begin]
        if categories_amount > 1:
            context['flag_section'] = True
        else:
            context['flag_section'] = False
        # FlagSection [Finish]

        # AmountActivation [Begin]
        if categories_amount < 5:
            context['flag_amount'] = True
            context['categories_amount'] = categories_amount
        else:
            context['flag_amount'] = False
            context['categories_amount'] = 4
        # AmountActivation [Finish]

        #figure = folium.Figure()
        #m = folium.Map(width='100%',height='100%',location=[-33.4569397, -70.6482697], zoom_start=12, tiles='Stamen Toner')
        #m.add_to(figure)
        #for item in context['capsule_list']:
        #    if item.lat and item.lng:
        #        folium.Marker(location=[item.lat, item.lng], popup=item.name, icon=folium.Icon(icon='cloud')).add_to(m)
        #figure = figure._repr_html_()
        #figure.save('map.html')
        #print(figure)
        #mapWidth = 600
        #mapHeight = 600
        #srcdoc = m.HTML.replace('"', '&quot;')
        #embed = HTML('<iframe srcdoc="{}" '
        #     'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
        #     'border: none"></iframe>'.format(figure, mapWidth, mapHeight))
        #context['map'] = embed

        return context

class AboutPageView(ListView):
    model = Category
    template_name = "core/about.html"
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['course_list'] = Course.objects.all()

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

class DisplayPageView(TemplateView):
    template_name = "core/display.html"

class MapDisplayView(TemplateView):
    model = Capsule
    template_name = "core/map_display.html"
    context_object_name = 'capsule_list'

    def get_context_data(self, **kwargs):
        context = super(MapDisplayView, self).get_context_data(**kwargs)
        context['capsule_list'] = Capsule.objects.all()

        figure = folium.Figure()
        m = folium.Map(width='100%',height='100%',location=[-33.4569397, -70.6482697], zoom_start=12, tiles='Stamen Toner')
        m.add_to(figure)
        for item in context['capsule_list']:
            if item.lat and item.lng:
                folium.Marker(location=[item.lat, item.lng], popup=item.name, icon=folium.Icon(icon='cloud')).add_to(m)
        figure = figure.get_root().render()
        context['my_map'] = figure

        return context