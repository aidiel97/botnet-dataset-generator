import pandas as pd
import dask.dataframe as dd

from dataLoader import *
urlExtractData = '../extract/ctu/'
urlExtractDataNCC = '../extract/ncc/'

def simulation(sensorId, a,b,c,d,e,f,g):
    bot_dfa = loadSplitActivity(urlExtractDataNCC, a, 'botnet')
    bot_dfb = loadSplitActivity(urlExtractDataNCC, b, 'botnet')
    bot_dfc = loadSplitActivity(urlExtractDataNCC, c, 'botnet')
    bot_dfd = loadSplitActivity(urlExtractDataNCC, d, 'botnet')
    bot_dfe = loadSplitActivity(urlExtractDataNCC, e, 'botnet')
    bot_dff = loadSplitActivity(urlExtractDataNCC, f, 'botnet')
    bot_dfg = loadSplitActivity(urlExtractDataNCC, g, 'botnet')

    normal_dfa = loadSplitActivity(urlExtractDataNCC, a, 'normal')
    normal_dfb = loadSplitActivity(urlExtractDataNCC, b, 'normal')
    normal_dfc = loadSplitActivity(urlExtractDataNCC, c, 'normal')
    normal_dfd = loadSplitActivity(urlExtractDataNCC, d, 'normal')
    normal_dfe = loadSplitActivity(urlExtractDataNCC, e, 'normal')
    normal_dff = loadSplitActivity(urlExtractDataNCC, f, 'normal')
    normal_dfg = loadSplitActivity(urlExtractDataNCC, g, 'normal')
    print('datasets loaded')

    botList = [bot_dfa,bot_dfb,bot_dfc,bot_dfd,bot_dfe,bot_dff,bot_dfg]
    normalList = [normal_dfd,normal_dfe,normal_dff,normal_dfg]
    allList = botList + normalList

    #concat
    df_bot = pd.concat(botList)
    df_normal = pd.concat(normalList)
    df_result = pd.concat(allList)
    print('dataset concated')

    #adding sensor id
    df_bot['sensorId'] = sensorId
    df_normal['sensorId'] = sensorId
    df_result['sensorId'] = sensorId

    #sort by StartTime
    df_bot.sort_values(by='syntheticTime', inplace=True)
    df_bot.reset_index(drop=True, inplace=True)

    df_normal.sort_values(by='syntheticTime', inplace=True)
    df_normal.reset_index(drop=True, inplace=True)

    df_result.sort_values(by='syntheticTime', inplace=True)
    df_result.reset_index(drop=True, inplace=True)
    print('sorting success')

    #formatting
    df_bot['StartTime'] = df_bot['syntheticTime']
    df_bot.drop('diff', inplace=True, axis=1)
    df_bot.drop('syntheticTime', inplace=True, axis=1)
    df_bot.to_csv('../result/sensor'+str(sensorId)+'_botnet-only.binetflow', index=False)
    print('storing data bot success')

    df_normal['StartTime'] = df_normal['syntheticTime']
    df_normal.drop('diff', inplace=True, axis=1)
    df_normal.drop('syntheticTime', inplace=True, axis=1)
    df_normal.to_csv('../result/sensor'+str(sensorId)+'_normal-only.binetflow', index=False)
    print('storing data normal success')

    df_result['StartTime'] = df_result['syntheticTime']
    df_result.drop('diff', inplace=True, axis=1)
    df_result.drop('syntheticTime', inplace=True, axis=1)
    df_result.to_csv('../result/sensor'+str(sensorId)+'.binetflow', index=False)
    print('storing all data success')

def mergingAllSensors():
    sensorAll = open('../result/all-sensors.binetflow', 'a')
    sensor1 = open('../result/sensor1.binetflow', 'r')
    sensor2 = open('../result/sensor2.binetflow', 'r')
    sensor3 = open('../result/sensor3.binetflow', 'r')

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
    df = dd.read_csv('../result/all-sensors.binetflow',dtype={
            'Dur': 'object',
            'SrcBytes': 'object',
            'TotBytes': 'object',
            'TotPkts': 'object',
            'activityLabel': 'object',
            'dTos': 'object',
            'sTos': 'object',
            'sensorId': 'object',
            'Dport':'object',
            'Sport':'object'
        })

    sorted_df = df.sort_values("StartTime")
    print('sorting success')

    #storing data with dask
    sorted_df.to_csv('../result/all-sensors.binetflow', single_file=True, index=False)
    print('storing data success')