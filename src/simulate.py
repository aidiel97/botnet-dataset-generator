import os
import pandas as pd
import dask.dataframe as dd
import random

from utilities.common import *
from utilities.dataLoader import *

def simulation(sensorId, a,b,c,d,e,f,g):
    print("\n====================================Simulation for Sensor "+str(sensorId)+" START==")

    botList = []
    for dataframes in [a,b,c,d,e,f,g]:
        bot_df = loadSplitActivity(urlExtractDataNCC, dataframes, 'botnet')
        botList.append(bot_df)
    print('--------------------------------bot datasets loaded')

    normalList = []
    listNormalForLoad = random.sample([a,b,c,d,e,f,g], 4)
    for dataframes in listNormalForLoad:
        if(listNormalForLoad.index(dataframes) == sensorId):
            normal_df = loadSplitActivity(urlExtractDataNCC, dataframes, 'normal')
        else:
            normal_df = loadSplitActivity(urlExtractData, dataframes, 'normal')
        normalList.append(normal_df)
    print('--------------------------------normal datasets loaded')

    #merge all list
    allList = botList + normalList

    #concat
    df_bot = pd.concat(botList)
    df_normal = pd.concat(normalList)
    df_result = pd.concat(allList)
    print('...dataset concated!')

    #adding sensor id
    df_bot['SensorId'] = sensorId
    df_normal['SensorId'] = sensorId
    df_result['SensorId'] = sensorId

    #sort by StartTime
    df_bot.sort_values(by='SyntheticTime', inplace=True)
    df_bot.reset_index(drop=True, inplace=True)

    df_normal.sort_values(by='SyntheticTime', inplace=True)
    df_normal.reset_index(drop=True, inplace=True)

    df_result.sort_values(by='SyntheticTime', inplace=True)
    df_result.reset_index(drop=True, inplace=True)
    print('...sorting success!')

    #formatting
    df_bot['StartTime'] = df_bot['SyntheticTime']
    df_bot.drop('Diff', inplace=True, axis=1)
    df_bot.drop('SyntheticTime', inplace=True, axis=1)
    df_bot.drop('Limit', inplace=True, axis=1)
    df_bot.to_csv('result/sensor'+str(sensorId)+'/sensor'+str(sensorId)+'_botnet-only.binetflow', index=False)
    print('...bot data stored!')

    df_normal['StartTime'] = df_normal['SyntheticTime']
    df_normal.drop('Diff', inplace=True, axis=1)
    df_normal.drop('SyntheticTime', inplace=True, axis=1)
    df_normal.drop('Limit', inplace=True, axis=1)
    df_normal.to_csv('result/sensor'+str(sensorId)+'/sensor'+str(sensorId)+'_normal-only.binetflow', index=False)
    print('...normal data stored!')

    df_result['StartTime'] = df_result['SyntheticTime']
    df_result.drop('Diff', inplace=True, axis=1)
    df_result.drop('SyntheticTime', inplace=True, axis=1)
    df_result.drop('Limit', inplace=True, axis=1)
    df_result.to_csv('result/sensor'+str(sensorId)+'/sensor'+str(sensorId)+'.binetflow', index=False)
    print('...all data stored!')
    
    print("====================================Simulation for Sensor "+str(sensorId)+" END==")

def mergingAllSensors():
    print("\n====================================Merging Process START==")
    sensorAll = open('result/all-sensors/sensors-all.binetflow', 'a')
    sensor1 = open('result/sensor1/sensor1.binetflow', 'r')
    sensor2 = open('result/sensor2/sensor2.binetflow', 'r')
    sensor3 = open('result/sensor3/sensor3.binetflow', 'r')

    print('start merging data from sensors')
    for sensors in [sensor1, sensor2, sensor3]:
        for line in sensors:
            sensorAll.write(line)
    
    print('success merging all sensors')
    sensorAll.close()
    sensor1.close()
    sensor2.close()
    sensor3.close()

    # sorting with dask
    df = dd.read_csv('result/all-sensors/sensors-all.binetflow',dtype=csvDType)

    sorted_df = df.sort_values("StartTime")
    print('sorting success')

    #storing data with dask
    sorted_df.to_csv('result/all-sensors/sensors-all.binetflow', single_file=True, index=False)
    print('storing data success')
    
    print("====================================Merging Process END==")

def analytics(sensor):
    print("\n====================================Analysis for Sensor "+str(sensor)+" START==")
    idSensor = sensor
    if(str(idSensor) == 'all'):
        fileName = 'result/all-sensors/sensors-all.binetflow' #load from generator
        txtFile = 'result/all-sensors/sensors-all.txt'
        detailHour = 'result/all-sensors/sensors-all-detail-hours.png'
        detailMinutes = 'result/all-sensors/sensors-all-detail-minutes.png'
    else:
        detailHour = 'result/sensor'+str(idSensor)+'/sensor'+str(idSensor)+'-detail-hours.png'
        detailMinutes = 'result/sensor'+str(idSensor)+'/sensor'+str(idSensor)+'-detail-minutes.png'
        txtFile = 'result/sensor'+str(idSensor)+'/sensor'+str(idSensor)+'.txt'
        fileName = 'result/sensor'+str(idSensor)+'/sensor'+str(idSensor)+'.binetflow' #load from generator
    raw_df=pd.read_csv(fileName)
    raw_df['StartTimeHour'] = raw_df['StartTime'].str[:13]
    raw_df['StartTimeMinute'] = raw_df['StartTime'].str[:16]
    
    normal_df=raw_df[raw_df['ActivityLabel'].isin([0])]
    bot_df=raw_df[raw_df['ActivityLabel'].isin([1])]
    
    with open(txtFile, 'w') as f:
        total = normal_df.shape[0] + bot_df.shape[0]
        bot_percent = bot_df.shape[0]/total*100
        normal_percent = normal_df.shape[0]/total*100

        f.write('\ntotal traffic: '+str(total))
        f.write('\nbot traffic: '+str(bot_df.shape[0])+' ('+str(bot_percent)+'%)')
        f.write('\nnormal traffic: '+str(normal_df.shape[0])+' ('+str(normal_percent)+'%)')

    print(txtFile+' created!')

    #groupbyhour
    botgroup_df = bot_df.groupby(['StartTimeHour'])['StartTime'].count().reset_index(name='bot')
    botgroup_df['Hour'] = botgroup_df.index

    normalgroup_df = normal_df.groupby(['StartTimeHour'])['StartTime'].count().reset_index(name='normal')
    normalgroup_df['Hour'] = normalgroup_df.index

    ax = botgroup_df.plot(x="Hour", y="bot", color="red")
    normalgroup_df.plot(ax=ax, x="Hour", y="normal", color="green", title="Sensor "+str(idSensor)+" Detail in Hours")

    ax.set_xlabel("Hours")
    ax.set_ylabel("Activity Count")
    ax.figure.savefig(detailHour, transparent=False)
    print(detailHour+' created!')

    #groupbyMinutes
    botgroup_df = bot_df.groupby(['StartTimeMinute'])['StartTime'].count().reset_index(name='bot')
    botgroup_df['Minute'] = botgroup_df.index

    normalgroup_df = normal_df.groupby(['StartTimeMinute'])['StartTime'].count().reset_index(name='normal')
    normalgroup_df['Minute'] = normalgroup_df.index

    ax = botgroup_df.plot(x="Minute", y="bot", color="red")
    normalgroup_df.plot(ax=ax, x="Minute", y="normal", color="green", title="Sensor "+str(idSensor)+" Detail in Minutes")

    ax.set_xlabel("Minutes")
    ax.set_ylabel("Activity Count")
    ax.figure.savefig(detailMinutes, transparent=False)
    print(detailMinutes+' created!')

    print("====================================Analysis for Sensor "+str(sensor)+" END==")

#simulation
def simulate():
    simulation(1, 3,10,1,2,7,12,5)
    analytics(1)
    simulation(2, 10,11,1,2,9,6,13)
    analytics(2)
    simulation(3, 3,4,9,8,12,5,13)
    analytics(3)

#merging sensors
def merge():
    mergingAllSensors()
    analytics('all')