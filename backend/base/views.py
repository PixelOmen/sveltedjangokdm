from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def csrf_token(request):
    response = JsonResponse({'csrf_token': get_token(request)})
    return response

# Create your views here.
class TestList(ListView):
    template_name = 'base/test_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Test List'
        return context
    
def test_response(request):
    return HttpResponse('Test Response')