from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Custom form styling
class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add classes to form fields
        form.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        form.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
        return form


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = StyledUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('login')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Style form fields
        form.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task title'
        })
        form.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task description (optional)',
            'rows': 4
        })
        form.fields['complete'].widget.attrs.update({
            'class': 'form-checkbox'
        })
        return form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Style form fields
        form.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task title'
        })
        form.fields['description'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task description (optional)',
            'rows': 4
        })
        form.fields['complete'].widget.attrs.update({
            'class': 'form-checkbox'
        })
        return form


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_confirm_delete.html'