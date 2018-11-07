# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import FileResponse, Http404
from personal.models import Project
import os
from apixu.client import ApixuClient, ApixuException


def index(request):
    try:
        api_key = 'df82bbb6f1fa4313ae7215742180611'
        client = ApixuClient(api_key)
        current = client.getCurrentWeather(q='Ljubljana')
        country = current['location']['country']
        temp = current['current']['temp_c']
        wind = current['current']['wind_degree']
    except ApixuException:
        country = None
        temp = None
        wind = None

    projects = Project.objects.order_by('-posted')[:3]
    contex = {'projects': projects, 'weather': current, 'wind': wind, 'location': country, 'temp': temp}

    return render(request, "index.html", contex)


def projects(request):
    projects = Project.objects.order_by('-posted')
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def download_pdf(request):
    try:
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "media/rok_zabukovec_zivljenjepis2018.pdf"
        abs_file_path = os.path.join(script_dir, rel_path)
        return FileResponse(open(abs_file_path, 'rb'), content_type='application/pdf')
    except OSError:
        raise Http404()
