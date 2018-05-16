from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    # urls for Organization
    path(
        'organization/',
        views.OrganizationListView.as_view(),
        name='organization_list'),
    path(
        'organization/create/',
        views.OrganizationCreateView.as_view(),
        name='organization_create'),
    path(
        'organization/detail/<slug:slug>/',
        views.OrganizationDetailView.as_view(),
        name='organization_detail'),
    path(
        'organization/update/<slug:slug>/',
        views.OrganizationUpdateView.as_view(),
        name='organization_update'),
]
