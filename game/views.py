from django.shortcuts import render
from django.views import View


class LaunchView(View):

    def get(self, request):
        return render(request, 'launcher.html')

    def post(self, request):
        return render(request, 'launcher.html')
