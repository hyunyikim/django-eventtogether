from django.views import generic
from .models import Events

# 클래스형 뷰
class IndexView(generic.ListView):
    print('indexView 진입')
    template_name = 'events/index.html'
    model = Events

class DetailView(generic.DetailView):
    template_name = 'events/detail.html'
    model = Events
