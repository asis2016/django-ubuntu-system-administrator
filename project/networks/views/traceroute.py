from django.shortcuts import render
import subprocess
from ..forms import *


def trace_route(response):
    """ traceroute: the route packets trace to network hosts. """
    if response.method == "POST":
        form = TraceRoute(response.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            #print(url)

        logs = subprocess.Popen(['/bin/bash', '-c',  f'traceroute {url}'], stdout=subprocess.PIPE)
        logs = logs.stdout.readlines()

        new_logs = []
        for log in logs:
            new_logs.append(log.decode("utf-8"))

        context = {'form': form, 'logs': new_logs}
    else:
        form = TraceRoute()
        context = {'form': form}

    template = 'traceroute/trace-route.html'

    return render(response, template, context)


def trace_route_request(request):
    if request.method == "POST":
        print(request.POST)

        # subprocess
        form = TraceRoute()
        result = subprocess.Popen(['/bin/bash', '-c',  'traceroute', 'www.google.com'])

    # with open('./trace-route.out', 'r') as route_logs:
    # logs = route_logs.readlines()

    context = {'form': form}

    return render(request, 'traceroute/trace-route.html', {'form': form})
