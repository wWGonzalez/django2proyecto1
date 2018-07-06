from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

class OtroView(TemplateView):
    template_name='otro.html'



def main_page(request):
    return render(request,'index.html')
