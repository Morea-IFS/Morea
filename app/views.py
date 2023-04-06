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


def api(request):
    if request.method == 'GET':
        consumoAtual = request.GET['consumoAtual']
        consumoTotal = request.GET['consumoTotal']
        localColeta = request.GET['localColeta']
        nodeID = request.GET['nodeID']

        coletas = Data(mote=nodeID, last_collection=consumoAtual,
                       total=consumoTotal)
        coletas.save()

        print(consumoAtual, consumoTotal, localColeta, nodeID)

    return render(request, 'api.html')
