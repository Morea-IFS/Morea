from app.models import Motes, Data, StatsHour
from django.utils import timezone
from datetime import timedelta
import numpy


def run():
    oneHourCounter = timezone.now() - timedelta(hours=1)
    wMotes = Motes.objects.values_list('id').filter(type=1)

    for mote in wMotes:
        try:
            wMotesData = list(Data.objects.values_list('last_collection').filter(
                collect_date__gte=oneHourCounter, mote=mote))
            # Função __gte = greater than or equal, compara a data.

            wMean = numpy.mean(wMotesData)
            wMedian = numpy.median(wMotesData)
            wSTD = numpy.std(wMotesData)
            wCV = wSTD / wMean
            wMax = numpy.amax(wMotesData)
            wMin = numpy.amin(wMotesData)
            wFQ = numpy.quantile(wMotesData, 0.25)
            wTQ = numpy.quantile(wMotesData, 0.75)
            stats = StatsHour(mote=Motes.objects.get(
                id=mote[0]), mean=wMean, median=wMedian, std=wSTD, cv=wCV, max=wMax, min=wMin, fq=wFQ, tq=wTQ)
            stats.save()
        except:
            pass
