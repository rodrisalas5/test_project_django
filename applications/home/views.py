from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Home
from .forms import TestFormHome
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'home/home.html'

class SuccessViewHome(TemplateView):
    template_name = "person/success.html"

class HomeCreateView(CreateView):
    model = Home
    template_name = 'home/addHome.html'
    form_class = TestFormHome
    # fields = ['title', 'subtitle', 'quantity']
    success_url = reverse_lazy('home_app:correct')    

class TestViewHome(TemplateView):
    template_name = "home/test.html" 

class NavbarViewHome(TemplateView):
    template_name = "home/common/navbar.html" 

class MenuViewHome(TemplateView):
    template_name = "home/common/menu.html" 

class footerViewHome(TemplateView):
    template_name = "home/common/footer.html" 