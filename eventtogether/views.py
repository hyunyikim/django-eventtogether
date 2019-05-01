from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    # 만약 보낼 데이터가 있다면?
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = {'app': 'event together!'}
        return context
