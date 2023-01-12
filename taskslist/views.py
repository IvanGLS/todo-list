from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Task, Tag
from .forms import TaskForm, TagForm

class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    ordering = ["-created_date"]
    paginate_by = 6
    template_name = "taskslist/index.html"
    queryset = Task.objects.all()

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks-list")

class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")

class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks-list")

class TagsListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "taskslist/tags_list.html"
    paginate_by = 6

class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")

class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tags-list")

class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tags-list")


@login_required
def task_complete(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed is True:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:tasks-list"))
