from django.shortcuts import render

# Create your views here.
from todo.models import Todo
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView,ListView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoListView(ListView):
    template_name = 'todo/list.html'
    model = Todo
    context_object_name = 'Todo_list'

class TodoCreateView(CreateView, LoginRequiredMixin):
    template_name = 'todo/create.html'
    model = Todo
    fields = ("title","description","limit")
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list')

    


class TodoDetailView(DetailView):
    template_name = 'todo/detail.html'
    model = Todo
    context_object_name = 'Todo_detail'


class TodoUpdateView(UpdateView):
    template_name = 'todo/update.html'
    model = Todo
    fields = ("title","description","limit")
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    




class TodoDeleteView(DeleteView):
    template_name = 'todo/delete.html'
    model = Todo
    success_url = reverse_lazy('list')
