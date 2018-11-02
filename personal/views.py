# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import FileResponse, Http404
from personal.models import Project
import os


def index(request):
    projects = Project.objects.order_by('-posted')
    contex = {'projects': projects}
    return render(request, "index.html", contex)


def download_pdf(request):
    try:
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "media/mypdf.pdf"
        abs_file_path = os.path.join(script_dir, rel_path)
        return FileResponse(open(abs_file_path, 'rb'), content_type='application/pdf')
    except OSError:
        raise Http404()
