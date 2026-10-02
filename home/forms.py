from django import forms
from .models import Project, Testimony, TechStack


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = [
            'project_name',
            'description',
            'tech_stack',
            'link'
        ]

        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Project Name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Project Description'
            }),

            'tech_stack': forms.CheckboxSelectMultiple(),

            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
        }


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony

        fields = [
            'full_name',
            'content'
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your feedback/testimony here...'
            }),
        }


class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack

        fields = [
            'name'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tech stack name'
            }),
        }


class DashboardProjectForm(forms.Form):

    project_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Project Name'
        })
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Project Description'
        })
    )

    tech_stack = forms.ModelChoiceField(
        queryset=TechStack.objects.all(),
        required=True,
        empty_label=None,
        widget=forms.RadioSelect
    )

    link = forms.URLField(
        required=True,
        widget=forms.URLInput(attrs={
            'placeholder': 'https://example.com'
        })
    )