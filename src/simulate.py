import pandas as pd
import glob
import os
from datetime import datetime, timedelta
from dataLoader import *
urlExtractData = '../extract/ctu/'
urlExtractDataNCC = '../extract/ncc/'

def simulation(sensorId, a,b,c,d,e,f,g):
    bot_dfa = loadSplitActivity(urlExtractData, a, 'botnet')
    bot_dfb = loadSplitActivity(urlExtractData, b, 'botnet')
    bot_dfc = loadSplitActivity(urlExtractData, c, 'botnet')
    bot_dfd = loadSplitActivity(urlExtractData, d, 'botnet')
    bot_dfe = loadSplitActivity(urlExtractData, e, 'botnet')
    bot_dff = loadSplitActivity(urlExtractData, f, 'botnet')
    bot_dfg = loadSplitActivity(urlExtractData, g, 'botnet')

    normal_dfa = loadSplitActivity(urlExtractDataNCC, a, 'normal')
    normal_dfb = loadSplitActivity(urlExtractDataNCC, b, 'normal')
    normal_dfc = loadSplitActivity(urlExtractDataNCC, c, 'normal')
    normal_dfd = loadSplitActivity(urlExtractDataNCC, d, 'normal')
    normal_dfe = loadSplitActivity(urlExtractDataNCC, e, 'normal')
    normal_dff = loadSplitActivity(urlExtractDataNCC, f, 'normal')
    normal_dfg = loadSplitActivity(urlExtractDataNCC, g, 'normal')
    print('datasets loaded')

    botList = [bot_dfa,bot_dfb,bot_dfc,bot_dfd,bot_dfe,bot_dff,bot_dfg]
    normalList = [ normal_dfa,normal_dfb,normal_dfc,normal_dfd,normal_dfe,normal_dff,normal_dfg]
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
    # setting the path for joining multiple files
    files = os.path.join("C:/its/6-code/botnetDatasetGenerator/result/", "sensor*.binetflow")

    # list of merged files returned
    files = glob.glob(files)

    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)
    print(df)