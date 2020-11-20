from django.urls import path

from status.views.basic import status_list, status_progress, status_match


urls = [
    path('', status_list, name='index'),
    path('progress', status_progress, name='status_progress'),
    path('match', status_match, name='status_match'),
]