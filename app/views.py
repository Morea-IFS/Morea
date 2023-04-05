from django.shortcuts import render
from app.models import Data
from .statistics.graphic import addDatasInDatasPD, createDataFrame, addGraphicsInHTML


def home(request):
    return render(request, 'home/home.html')


def dashboard(request):
    datas = Data.objects.select_related('mote').all()

    datasPD = {
        'energy': {},
        'water': {}
    }

    addDatasInDatasPD(datas, datasPD)

    createDataFrame(datasPD)

    objectDatasHTML = addGraphicsInHTML()

    return render(request, 'dashboard/dashboard.html', {
        'listPathsHTML': objectDatasHTML[0],
        'listNamesFilesHTML': objectDatasHTML[1]
    })


def updates(request):
    return render(request, 'updates/updates.html')


def about(request):
    return render(request, 'about/about.html')
