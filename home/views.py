from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from .models import (
    Project,
    PersonalInformation,
    Testimony,
    Inquiry,
    TechStack
)

from .forms import (
    ProjectForm,
    TestimonyForm,
    TechStackForm,
    DashboardProjectForm
)


# =========================================================
# SUPERUSER CHECK
# =========================================================

def superuser_required(user):
    return user.is_authenticated and user.is_superuser


# =========================================================
# PUBLIC PORTFOLIO VIEWS
# =========================================================

def project_list(request):
    projects = Project.objects.all()

    return render(
        request,
        'home/project_list.html',
        {
            'projects': projects
        }
    )


def project_detail(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk
    )

    return render(
        request,
        'home/project_detail.html',
        {
            'project': project
        }
    )


def personal_info(request):
    info = PersonalInformation.objects.first()

    return render(
        request,
        'home/personal_info.html',
        {
            'info': info
        }
    )


# =========================================================
# OLD ADD PROJECT VIEW
# NOW ALSO SUPERUSER ONLY
# =========================================================

@user_passes_test(
    superuser_required,
    login_url='admin_login'
)
def add_project(request):

    if request.method == 'POST':

        form = ProjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('project_list')

    else:

        form = ProjectForm()

    return render(
        request,
        'home/add_project.html',
        {
            'form': form
        }
    )


# =========================================================
# CONTACT / INQUIRY
# =========================================================

def contact_view(request):

    if request.method == 'POST':

        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message'),
        )

        return redirect('contact')

    return render(
        request,
        'home/contact.html'
    )


# =========================================================
# TESTIMONIES
# =========================================================

def add_testimony(request):

    if request.method == 'POST':

        form = TestimonyForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('testimony_list')

    else:

        form = TestimonyForm()

    return render(
        request,
        'home/add_testimony.html',
        {
            'form': form
        }
    )


class TestimonyListView(ListView):

    model = Testimony

    template_name = 'home/testimony_list.html'

    context_object_name = 'testimonies'


def testimony_detail(request, pk):

    testimony = get_object_or_404(
        Testimony,
        pk=pk
    )

    return render(
        request,
        'home/testimony_detail.html',
        {
            'testimony': testimony
        }
    )


# =========================================================
# QUIZ 5 & 6
# ADMIN / SUPERUSER LOGIN
# =========================================================

def admin_login(request):

    # If already logged in as a superuser,
    # go directly to dashboard.
    if (
        request.user.is_authenticated
        and request.user.is_superuser
    ):
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        # Only superusers are allowed.
        if user is not None and user.is_superuser:

            login(request, user)

            return redirect('dashboard')

        messages.error(
            request,
            'Invalid username/password or this account is not a superuser.'
        )

    return render(
        request,
        'home/admin_login.html'
    )


# =========================================================
# DASHBOARD
# =========================================================

@user_passes_test(
    superuser_required,
    login_url='admin_login'
)
def dashboard(request):

    projects = Project.objects.all()

    tech_stacks = TechStack.objects.all()

    context = {
        'projects': projects,
        'tech_stacks': tech_stacks,
    }

    return render(
        request,
        'home/dashboard.html',
        context
    )


# =========================================================
# CREATE TECH STACK
# =========================================================

@user_passes_test(
    superuser_required,
    login_url='admin_login'
)
def create_tech_stack(request):

    if request.method == 'POST':

        form = TechStackForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    else:

        form = TechStackForm()

    return render(
        request,
        'home/create_tech_stack.html',
        {
            'form': form
        }
    )


# =========================================================
# CREATE PROJECT
# =========================================================

@user_passes_test(
    superuser_required,
    login_url='admin_login'
)
def create_project(request):

    if request.method == 'POST':

        form = DashboardProjectForm(request.POST)

        if form.is_valid():

            project = Project.objects.create(
                project_name=form.cleaned_data['project_name'],
                description=form.cleaned_data['description'],
                link=form.cleaned_data['link']
            )

            project.tech_stack.add(
                form.cleaned_data['tech_stack']
            )

            return redirect('dashboard')

    else:

        form = DashboardProjectForm()

    return render(
        request,
        'home/create_project.html',
        {
            'form': form
        }
    )


# =========================================================
# LOGOUT
# =========================================================

def admin_logout(request):

    logout(request)

    return redirect('admin_login')