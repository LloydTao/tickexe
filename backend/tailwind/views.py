from django.shortcuts import render
from django.views.generic.base import TemplateView


class TailwindView(TemplateView):

    template_name = "tailwind/example.html"
