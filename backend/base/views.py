from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView

class SvelteAppView(TemplateView):
    template_name = 'index.html'

class TestList(ListView):
    template_name = 'base/test_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Test List'
        return context
    
def test_response(request):
    return JsonResponse({'test': 'my response'})