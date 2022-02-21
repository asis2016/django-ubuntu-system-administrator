from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess


class NetworkView(TemplateView):
    template_name = 'networks/networks.html'


def external(request):
    if request.method == "POST":
        print(request.POST)

        # subprocesses
        txt = subprocess.check_output(['ping', 'www.google.com', '-c', '4'])

    return render(request, 'networks/networks.html', {
        'data': txt
    })
