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
        try:
            event = Events()
            event.eid = Events.objects.order_by('eid').last().eid + 1
            event.ename = request.POST['ename']
            event.econtent = request.POST['econtent']
            event.ecreater = request.POST['ecreater']
            event.eloc = request.POST['eloc']
            event.eprice = request.POST['eprice']
            event.emaxattendee = request.POST['emaxattendee']
            event.save()
            return HttpResponseRedirect(reverse('events:detail', args=(event.eid,)))
        except():
            return render(request, 'events/write.html', {'error_message': 'write failed'})
    return render(request, 'events/write.html')

def update(request, eid):
    event = Events.objects.get(pk=eid)
    if request.method == 'POST':
        try:
            event = Events(eid=request.POST['eid'])
            event.eid = request.POST['eid']
            event.ename = request.POST['ename']
            event.econtent = request.POST['econtent']
            event.ecreater = request.POST['ecreater']
            event.eloc = request.POST['eloc']
            event.emaxattendee = request.POST['emaxattendee']
            event.save()
            return HttpResponseRedirect(reverse('events:detail', args=(event.eid,)))
        except(KeyError, Events.DoesNotExist):
            return render(request, 'events/write.html', {
                'event':event,
                'error_message':'update failed'
            })
    return render(request, 'events/write.html', {'event':event})

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