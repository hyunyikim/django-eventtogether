from django.views import generic
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Events

# 클래스형 뷰



class DetailView(generic.DetailView):
    template_name = 'events/detail.html'
    model = Events


class WriteView(generic.View):
    template_name = 'events/write.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(selfs, request, *args, **kwargs):
        try:
            event = Events()
            event.eid = Events.objects.order_by('eid').last().eid + 1
            event.ename = request.POST['ename']
            event.econtent = request.POST['econtent']
            event.ecreater = request.POST['ecreater']
            event.estartdt = request.POST.get('estartdt')
            event.eenddt = request.POST.get('eenddt')
            event.eloc = request.POST['eloc']
            event.eprice = request.POST['eprice']
            event.emaxattendee = request.POST['emaxattendee']
            event.save()
            return HttpResponseRedirect(reverse('events:detail', args=(event.eid, )))
        except():
            return render(request, 'events/write.html', {'error_message': 'write failed'})


class DeleteView(generic.View):
    def get(self, request, *args, **kwars):
        print('delete get function')
        eid = self.kwargs.get("pk")
        try:
            event = Events.objects.get(eid=eid)
            event.delete()
            return HttpResponseRedirect(reverse('events:index'))
        except(KeyError, Events.DoesNotExist):
            return render(request, 'events/detail.html', {
                'event':event,
                'error_message':'delete failed'
            })


class UpdateView(generic.View):
    def get(self, request, *args, **kwargs):
        print('update get function')
        eid = self.kwargs.get("pk")
        try:
            event = Events.objects.get(eid=eid)
            return render(request, 'events/write.html', {'event': event})

        except(KeyError, Events.DoesNotExist):
            return render(request, 'events/detail.html', {
                'event': event,
                'error_message': 'update failed'
            })

    def post(self, request, *args, **kwargs):
        print('update post function')

        try:
            event = Events()
            event.eid = Events.objects.order_by('eid').last().eid + 1
            event.ename = request.POST['ename']
            event.econtent = request.POST['econtent']
            event.ecreater = request.POST['ecreater']
            event.estartdt = request.POST.get('estartdt')
            event.eenddt = request.POST.get('eenddt')
            event.eloc = request.POST['eloc']
            event.eprice = request.POST['eprice']
            event.emaxattendee = request.POST['emaxattendee']
            event.save()
            return HttpResponseRedirect(reverse('events:detail', args=(event.eid,)))
        except():
            return render(request, 'events/write.html', {'error_message': 'update failed'})