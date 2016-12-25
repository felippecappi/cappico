from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
home = TemplateView.as_view(template_name='index.html')