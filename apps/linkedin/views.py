from django.shortcuts import render
from django.views.generic import TemplateView


class LinkedinView(TemplateView):
    template_name = 'common/linkedin.html'

