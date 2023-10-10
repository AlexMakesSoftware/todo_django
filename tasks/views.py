from django.views.generic import ListView, CreateView
from .models import Task
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks:list')

    def post(self, request, *args, **kwargs):
        print("Printing request META data:")
        for key, value in request.META.items():
            print(f"{key}: {value}")
            
        return super().post(request, *args, **kwargs)
