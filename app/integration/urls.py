from django.urls import path

from . import views

app_name = 'integration'
urlpatterns = [
    # urls for Integration
    path('', views.IntegrationListView.as_view(), name='integration_list'),
    path('create/', views.IntegrationCreateView.as_view(), name='integration_create'),
    path('detail/<slug:slug>/', views.IntegrationDetailView.as_view(), name='integration_detail'),
    path('update/<slug:slug>/', views.IntegrationUpdateView.as_view(), name='integration_update'),
]
