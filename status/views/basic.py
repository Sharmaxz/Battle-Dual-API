from django.http import Http404
from django.shortcuts import render

from games.hash.models import Hash


def status_list(request):
    if request.method == 'GET':
        return render(request, 'status/status_index.html')
    raise Http404


def status_progress(request):
    if request.method == 'GET':
        return render(request, 'status/status_progress.html', {'hashs': Hash.objects.all()})
    raise Http404


def status_match(request):
    if request.method == 'GET':
        return render(request, 'status/status_match.html', {'hash': Hash.objects.get(pk=request.GET['id'])})
    raise Http404
