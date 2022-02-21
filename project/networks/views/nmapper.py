from django.shortcuts import render


def nmapper(request):
    '''Nmap tool.'''
    return render(request, 'nmapper.html', {'yo': 'yo'})
