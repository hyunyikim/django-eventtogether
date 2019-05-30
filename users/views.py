from django.views import generic
from django.shortcuts import render
from django.apps import apps


class SignInView(generic.View):
    template_name = 'users/signin.html'

    def get(self, request):
        print('signinview 함수 진입')
        return render(request, self.template_name, {'error_message': 'hello, this is error_message'})

    def post(self, request):
        print()


class SignUpView(generic.View):
    template_name = 'users/signup.html'

    def get(self, request):
        return render(request, self.template_name, {'error_message': 'hello, this is error_message'})

    def post(self, request):
        print()