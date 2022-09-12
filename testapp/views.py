from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def test_view (request):
    return JsonResponse({'foo':'bar'})