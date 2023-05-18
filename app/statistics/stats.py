import numpy
from ..models import Motes, Data, StatsHour


def calcWaterStats():
    wMotes = Motes.objects.values_list('id').filter(type=1)

    for mote in wMotes:
        wMotesData = list(Data.objects.values_list('min_lh').filter(mote=mote))
        wMean = numpy.mean(wMotesData)
        wMedian = numpy.median(wMotesData)
        wSTD = numpy.std(wMotesData)
        wCV = wSTD / wMean
        wMax = numpy.amax(wMotesData)
        wMin = numpy.amin(wMotesData)
        wFQ = numpy.quantile(wMotesData, 0.25)
        wTQ = numpy.quantile(wMotesData, 0.75)
        stats = StatsHour(id=mote[0], mote=Motes.objects.get(id=mote[0]), mean=wMean,
                          median=wMedian, std=wSTD, cv=wCV, max=wMax, min=wMin, fq=wFQ, tq=wTQ)
        stats.save()
