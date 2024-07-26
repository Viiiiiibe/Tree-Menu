from django.shortcuts import render


def menus(request, active_slug=None):
    return render(request, 'index.html', {'active_slug': active_slug})

