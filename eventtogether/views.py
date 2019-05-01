from django.views import generic
from django.apps import apps


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    # 만약 보낼 데이터가 있다면?
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dictVerbose = {}
        for app in apps.get_app_configs():
            print('app : ', app.path)
            if 'site-packages' not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context['verbose_dict'] = dictVerbose
        return context
