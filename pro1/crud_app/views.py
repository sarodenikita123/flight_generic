from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Flight


class FlightCreate(CreateView):
    model = Flight
    fields = "__all__"


class FlightList(ListView):
    model = Flight


class FlightDetail(DetailView):
    model = Flight


class FlightUpdate(UpdateView):
    model = Flight
    fields = "__all__"
    success_url = "/"


class FlightDelete(DeleteView):
    model = Flight
    success_url = "/"
    template_name = "crud_app/flight_delete.html"


