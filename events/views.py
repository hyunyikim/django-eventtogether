from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Events


# 함수형 뷰
def index(request):
    events_list = Events.objects.all()
    return render(request, 'events/index.html', {'events_list':events_list})

def detail(request, eid):
    event = get_object_or_404(Events, pk=eid)
    return render(request, 'events/detail.html', {'event':event})

def new(request):
    if request.method == 'POST':
        event = Events(request.POST)
        print(request.POST['ename'])
    return render(request, 'events/write.html', {})

def update(request, eid):
    print()

def delete(request, eid):
    try:
        event = Events.objects.get(pk=eid)
    except(KeyError, Events.DoesNotExist):
        return render(request, 'events/detail.html', {
            'event': event,
            'error_message': 'delete failed'
        })
    else:
        event.delete()
    return HttpResponseRedirect(reverse('events:index'))