from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def home_index(request):
    return HttpResponse("Hello to django home index function")

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello to django home")

    def post(self, request):
        pass
