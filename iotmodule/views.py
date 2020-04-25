from django.views.generic.base import TemplateView
from django.shortcuts import render

class IotModuleView(TemplateView):

    template_name = "iotmodule/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi wehooo"})