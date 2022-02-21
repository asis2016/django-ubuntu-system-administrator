from django.shortcuts import render


def apache_access_log(request):
    """ Shows Apache2 access logs. """
    with open('/var/log/apache2/access.log', 'r') as access_logs:
        context = {'logs': reversed(access_logs.readlines())}
    return render(request, 'apache2/apache-access-logs.html', context)


def apache_error_log(request):
    """ Shows Apache2 error logs. """
    with open('/var/log/apache2/error.log', 'r') as error_logs:
        context = {
            'logs': reversed(error_logs.readlines()),
            'len_logs': len(error_logs.readlines())
        }
    return render(request, 'apache2/apache-error-logs.html', context)