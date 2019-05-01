from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView, RedirectView, TemplateView
from .models import Events


class IndexView(ListView):
    template_name = 'events/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Events.objects.all()


class DetailView(DetailView):
    model = Events
    template_name = 'events/detail.html'

'''
class WriteView(View):
    def get(self, request):
        template_name = 'events/write.html'
        #return reverse(request, 'events/write.html')

    def post(self, request):
        return ''
'''

'''
class WriteView(TemplateView):
    template_name = 'events/write.html'
'''


class WriteView(View):
    def get(self, request):
        return render(request, '/events/write.html')

