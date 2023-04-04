from django.shortcuts import render
from app.models import Data
from .statistics.graphic import addDatasInDatasPD, createDataFrame

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

    return render(request, 'dashboard/dashboard.html', {'datas': datas})


def updates(request):
    return render(request, 'updates/updates.html')


def about(request):
    return render(request, 'about/about.html')
