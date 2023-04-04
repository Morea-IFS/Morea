import pandas as pd
import plotly.graph_objects as go

def createPlotly( arrayToPlotly, nameToFileCreate ):

    templateHoverWater = '<i>Data</i>: %{x}' + \
        '<br><i>Consumo(L)</i>: %{y:.1f}L <extra></extra>'

    templateHoverEnergy = '<i>Data</i>: %{x}' + \
        '<br><i>Consumo(W)</i>: %{y:.1f}W <extra></extra>'

    if nameToFileCreate[0] in 'Ee':
            createPlotly = go.Figure(go.Scatter(  
                x=arrayToPlotly['Data'],
                y=arrayToPlotly['Valor'],
                mode='markers+lines',
                hovertemplate=templateHoverEnergy))
            
            createPlotly.update_layout(

                title='',
                xaxis=dict(
                    title='',
                    showticklabels=False,),
                yaxis=dict(
                    title='',
                    showticklabels=False,
                ),
                margin=dict(l=0, r=0, t=0, b=0, pad=100),
            )

            createPlotly.write_html(
                f"static/graphics/dashboard/energy/{nameToFileCreate}.html")
            
    elif nameToFileCreate[0] in 'Ww':
            print('oie')
            createPlotly = go.Figure(go.Scatter(  
                x=arrayToPlotly['Data'],
                y=arrayToPlotly['Valor'],
                mode='markers+lines',
                hovertemplate=templateHoverWater))
            
            createPlotly.update_layout(

                title='',
                xaxis=dict(
                    title='',
                    showticklabels=False,),
                yaxis=dict(
                    title='',
                    showticklabels=False,
                ),
                margin=dict(l=0, r=0, t=0, b=0, pad=100),
            )

            createPlotly.write_html(
                f"static/graphics/dashboard/water/{nameToFileCreate}.html")
    else:
        pass

def createDataFrame(objectDatas):
    typeEnergy = 'energy'
    typeWater = 'water'
    getNameMote = 0
    getArrayDatas = 1
    getDatesInArrayDatas = 0
    getValuesInArrayDatas = 1

    for energyItems in objectDatas[typeEnergy].items():
        dataFrameCreateEnergy = pd.DataFrame(  
            {'Data': energyItems[getArrayDatas][getDatesInArrayDatas], 'Valor': energyItems[getArrayDatas][getValuesInArrayDatas]})
        
        createPlotly(dataFrameCreateEnergy, energyItems[getNameMote])

    for waterItems in objectDatas[typeWater].items():
        dataFrameCreateWater = pd.DataFrame(  
            {'Data': waterItems[getArrayDatas][getDatesInArrayDatas], 'Valor': waterItems[getArrayDatas][getValuesInArrayDatas]})
        
        createPlotly(dataFrameCreateWater, waterItems[getNameMote])


def addDatasInDatasPD( objectRequestDB, objectDatasPD ):
    for data in objectRequestDB:
        dataMoteName = data.mote.name
        dataCollectDate = data.collect_date
        dataLastCollection = data.last_collection

        if data.mote.get_type_display() == 'EMote':

            try:
                objectDatasPD['energy'][dataMoteName] = [[* objectDatasPD['energy'][dataMoteName][0], dataCollectDate], [* objectDatasPD['energy'][dataMoteName][1], dataLastCollection]]
            except:
                objectDatasPD['energy'][dataMoteName] = [[],[]]
                objectDatasPD['energy'][dataMoteName][0].append(dataCollectDate)
                objectDatasPD['energy'][dataMoteName][1].append(dataLastCollection)

        elif data.mote.get_type_display() == 'WMote':

            try:
                objectDatasPD['water'][dataMoteName] = [[* objectDatasPD['energy'][dataMoteName][0], dataCollectDate], [* objectDatasPD['energy'][dataMoteName][1], dataLastCollection]]
            except:
                objectDatasPD['water'][dataMoteName] = [[],[]]
                objectDatasPD['water'][dataMoteName][0].append(dataCollectDate)
                objectDatasPD['water'][dataMoteName][1].append(dataLastCollection)
        
        else:
            pass