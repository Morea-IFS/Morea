from django.http import HttpResponse
from django.shortcuts import render
from app.models import Data, Motes
from .statistics.graphic import addDatasInDatasPD, createDataFrame, addGraphicsInHTML, mainGraphics


def home(request):
    return render(request, 'home/home.html')


def dashboard(request):
    datasRaw = Data.objects.select_related('mote').all()

    rawGraphics = mainGraphics(datasRaw, "app/templates/graphics/dashboard/rawDatas",
                               "app/templates/graphics/dashboard/rawDatas", "raw")

    return render(request, 'dashboard/dashboard.html', {
        'listPathsHTML': rawGraphics[0],
        'listNamesFilesHTML': rawGraphics[1]
    })


def updates(request):
    return render(request, 'updates/updates.html')


def about(request):
    return render(request, 'about/about.html')


def api(request):
    secretKeyConst = '7$WMX70b9$#9'

    if request.method == 'GET':
        secretKey = request.GET['secretKey']

        if (secretKey == secretKeyConst):
            nodeID = request.GET['nodeID']
            consumoAtual = request.GET['consumoAtual']

            moteID = Motes.objects.get(id=nodeID)
            totalCollections = list(
                Data.objects.values_list('total').order_by("id").filter(mote=moteID).reverse())
            if (Data.objects.filter(id=nodeID).exists()):
                totalCollectionsData = totalCollections[0][0] + \
                    float(consumoAtual)
                coletas = Data(mote=moteID, last_collection=consumoAtual,
                               total=totalCollectionsData)
                coletas.save()
            else:
                coletas = Data(mote=moteID, last_collection=consumoAtual,
                               total=consumoAtual)
                coletas.save()

    return render(request, 'api.html')


def returnGraphic(request, typeMote, moteId):

    if moteId < 10:
        moteId = f'0{moteId}'

    if typeMote == "energy":
        return render(request, f'graphics/dashboard/rawDatas/energy/Emote{moteId}.html')
    elif typeMote == "water":
        return render(request, f'graphics/dashboard/rawDatas/water/Wmote{moteId}.html')
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
