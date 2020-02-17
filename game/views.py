from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from .forms import GameLaunchForm
from urllib.parse import urlencode


class LaunchView(View):

    def get(self, request):
        return render(request, 'launcher.html')

    def post(self, request):
        form = GameLaunchForm(request.POST)
        if form.is_valid():
            form.cleaned_data.update({"host": True, "id": get_random_string(15)})
            return redirect(f'/fight?{urlencode(form.cleaned_data)}')
        return render(request, 'launcher.html')
