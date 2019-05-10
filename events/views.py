from django.views import generic
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Events

# 클래스형 뷰
class IndexView(generic.ListView):
    template_name = 'events/index.html'
    model = Events


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
            event.eloc = request.POST['eloc']
            event.eprice = request.POST['eprice']
            event.emaxattendee = request.POST['emaxattendee']
            event.save()
            return HttpResponseRedirect(reverse('events:detail', args=(event.eid, )))
        except():
            return render(request, 'events/write.html', {'error_message': 'write failed'})


class DeleteView(generic.View):
    print()


class UpdateView(generic.View):
    print()