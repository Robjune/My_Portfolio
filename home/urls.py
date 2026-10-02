from django.urls import path
from . import views


urlpatterns = [

    # =====================================================
    # QUIZ 1 & 2
    # =====================================================

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


    # =====================================================
    # QUIZ 3
    # =====================================================

    path(
        'projects/add/',
        views.add_project,
        name='add_project'
    ),

    path(
        'contact/',
        views.contact_view,
        name='contact'
    ),

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


    # =====================================================
    # QUIZ 5 & 6
    # =====================================================

    path(
        'signin/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'logout/',
        views.admin_logout,
        name='admin_logout'
    ),
]