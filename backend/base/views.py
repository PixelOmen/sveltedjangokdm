from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class TestList(ListView):
    template_name = 'base/test_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Test List'
        return context