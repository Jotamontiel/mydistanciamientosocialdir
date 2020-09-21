from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from .models import Device
from registration.models import Profile
from .forms import DeviceForm

class IotModuleView(TemplateView):

    template_name = "iotmodule/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi wehooo"})


class DeviceListView(ListView):
    model = Device
    template_name = 'iotmodule/device_list.html'
    paginate_by = 5


class DeviceDetailView(DetailView):
    model = Device
    template_name = 'iotmodule/device_detail.html'


class DeviceCreate(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'iotmodule/device_form.html'
    success_url = reverse_lazy('iotmodule:devices')

    # Search for profile instance
    def form_valid(self, form):
        form.instance.profile = Profile.objects.get(id=self.request.user.id)
        return super(DeviceCreate, self).form_valid(form)


class DeviceUpdate(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'iotmodule/device_update_form.html'

    def get_success_url(self):
        return reverse_lazy('iotmodule:devices') + '?okEdit'


class DeviceDelete(DeleteView):
    model = Device
    template_name = 'iotmodule/device_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('iotmodule:devices') + '?okDelete'