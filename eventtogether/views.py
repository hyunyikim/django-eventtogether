from django.views import generic
from django.apps import apps
from eventtogether.events.models import Events


class IndexView(generic.ListView):
    print('Index View 진입')
    template_name = 'events/index.html'
    model = Events