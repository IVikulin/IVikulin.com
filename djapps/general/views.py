#from django.shortcuts import render
from django.views.generic import TemplateView
from .models import AboutMe
from djapps.portfolio.models import Work, Skill


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['about_me'] = AboutMe.objects.first()
        context['skills'] = Skill.objects.all().order_by('group', 'order')
        context['works'] = Work.objects.all()
        return context 