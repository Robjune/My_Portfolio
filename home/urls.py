from django.urls import path
from . import views

urlpatterns = [
    # --- Quiz 1 & Quiz 2 Routes ---
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.personal_info, name='personal_info'),

    # --- Quiz 3 Required Routes ---
    path('projects/add/', views.add_project, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),
]