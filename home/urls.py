from django.urls import path
from . import views


urlpatterns = [

    # Homepage
    path(
        '',
        views.project_list,
        name='home'
    ),

    # Public Portfolio
    path(
        'projects/',
        views.project_list,
        name='project_list'
    ),

    path(
        'projects/<int:pk>/',
        views.project_detail,
        name='project_detail'
    ),

    path(
        'about/',
        views.personal_info,
        name='personal_info'
    ),

    # Old Project Creation
    path(
        'projects/add/',
        views.add_project,
        name='add_project'
    ),

    # Contact
    path(
        'contact/',
        views.contact_view,
        name='contact'
    ),

    # Testimonies
    path(
        'testimonies/',
        views.TestimonyListView.as_view(),
        name='testimony_list'
    ),

    path(
        'testimonies/add/',
        views.add_testimony,
        name='add_testimony'
    ),

    path(
        'testimonies/<int:pk>/',
        views.testimony_detail,
        name='testimony_detail'
    ),

    # Admin / Superuser Login
    path(
        'signin/',
        views.admin_login,
        name='admin_login'
    ),

    # Logout
    path(
        'logout/',
        views.admin_logout,
        name='admin_logout'
    ),

    # Dashboard
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # Create Tech Stack
    path(
        'dashboard/tech-stacks/create/',
        views.create_tech_stack,
        name='create_tech_stack'
    ),

    # Create Project
    path(
        'dashboard/projects/create/',
        views.create_project,
        name='create_project'
    ),
]