from django.http import HttpResponse
from django.shortcuts import render
from app.models import Data, Motes
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

        moteID = Motes.objects.get(id=nodeID)

        coletas = Data(mote=moteID, last_collection=consumoAtual,
                       total=consumoTotal)
        coletas.save()

        print(consumoAtual, consumoTotal, localColeta, nodeID)

    return render(request, 'api.html')


def returnGraphic(request, typeMote, moteId):

    if moteId < 10:
        moteId = f'0{moteId}'

    if typeMote == "energy":
        return render(request, f'graphics/dashboard/energy/Emote{moteId}.html')
    elif typeMote == "water":
        return render(request, f'graphics/dashboard/water/Wmote{moteId}.html')
    else:
        pass


def graphics(request, **kwargs):

    if kwargs.get('emote_id'):
        moteId = kwargs.get('emote_id')
        return returnGraphic(request, 'energy', moteId)

    elif kwargs.get('wmote_id'):
        moteId = kwargs.get('wmote_id')
        return returnGraphic(request, 'water', moteId)

    else:
        pass
