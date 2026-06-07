from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from tasks.models import Tag, Task
from django.urls import reverse_lazy
from tasks.forms import TaskForm


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class ToggleTaskView(generic.View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("tasks:task-list")
