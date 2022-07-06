from django.http import HttpResponse
from django.views.generic import TemplateView
 
 
class HomePageView(TemplateView):
    template_name = 'home.html'


def index(request):
    return HttpResponse("Hello World")