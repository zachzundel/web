from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import OrganizationForm
from .models import Organization


class OrganizationListView(ListView):
    model = Organization


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm


class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
