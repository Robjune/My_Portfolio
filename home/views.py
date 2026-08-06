from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from .models import Project, PersonalInformation, Testimony, Inquiry
from .forms import ProjectForm, TestimonyForm

# --- Public Views (Quiz 1 & 2) ---

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'home/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'home/project_detail.html', {'project': project})

def personal_info(request):
    info = PersonalInformation.objects.first()
    return render(request, 'home/personal_info.html', {'info': info})

# --- Owner Only Route (Quiz 3 Requirement) ---

@staff_member_required
def add_project(request):
    """Owner-only function to add new projects via Django Forms."""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'home/add_project.html', {'form': form})

# --- Public Visitor Routes (Quiz 3 Requirement) ---

def contact_view(request):
    """Public contact page for visitor inquiries using HTML Form."""
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
    return render(request, 'home/contact.html')

def add_testimony(request):
    """Public page for visitors to leave feedback using Django Forms."""
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'home/add_testimony.html', {'form': form})

class TestimonyListView(ListView):
    """Class-Based View listing all user testimonies."""
    model = Testimony
    template_name = 'home/testimony_list.html'
    context_object_name = 'testimonies'

def testimony_detail(request, pk):
    """Function-Based Detail View when clicking a testimony."""
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'home/testimony_detail.html', {'testimony': testimony})