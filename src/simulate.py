import pandas as pd
import glob
import os
from datetime import datetime, timedelta
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

    # normal_dfa = loadSplitActivity(urlExtractDataNCC, a, 'normal')
    # normal_dfb = loadSplitActivity(urlExtractDataNCC, b, 'normal')
    # normal_dfc = loadSplitActivity(urlExtractDataNCC, c, 'normal')
    normal_dfd = loadSplitActivity(urlExtractDataNCC, d, 'normal')
    normal_dfe = loadSplitActivity(urlExtractDataNCC, e, 'normal')
    normal_dff = loadSplitActivity(urlExtractDataNCC, f, 'normal')
    normal_dfg = loadSplitActivity(urlExtractDataNCC, g, 'normal')
    print('datasets loaded')

    botList = [bot_dfa,bot_dfb,bot_dfc,bot_dfd,bot_dfe,bot_dff,bot_dfg]
    normalList = [ normal_dfd,normal_dfe,normal_dff,normal_dfg]
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

import dask.dataframe as dd
import operator
import sys
import csv
def mergingAllSensors():
    # # setting the path for joining multiple files
    # files = os.path.join("C:/its/6-code/botnetDatasetGenerator/result/", "sensor*.binetflow")

    # # list of merged files returned
    # # files = glob.glob(files)
    # sensor1 = pd.read_csv('../result/sensor1.binetflow')
    # sensor2 = pd.read_csv('../result/sensor2.binetflow')
    # sensor3 = pd.read_csv('../result/sensor3.binetflow')

    # # joining files with concat and read_csv
    # df = pd.concat([sensor1, sensor2, sensor3])
    # print('concat success')

    # df.sort_values('StartTime')
    # df.reset_index(drop=True)
    # print('sorting success')

    # df.to_csv('allSensors.csv', index=False)
    # print('storing data success')

    # sensorAll = open('../result/all-sensors.binetflow', 'a')
    # sensor1 = open('../result/sensor1.binetflow', 'r')
    # sensor2 = open('../result/sensor2.binetflow', 'r')
    # sensor3 = open('../result/sensor3.binetflow', 'r')

    # print('start merging data from sensors')
    # for sensors in [sensor1, sensor2, sensor3]:
    #     for line in sensors:
    #         sensorAll.write(line)
    
    # print('success merging all sensors')
    # sensorAll.close()
    # sensor1.close()
    # sensor2.close()
    # sensor3.close()

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
    # df.reset_index(drop=True)
    sorted_df = df.sort_values("StartTime")
    print('sorting success')
    
    # sorted_df.reset_index(drop=True)
    
    #storing with pandas
    sorted_df.to_csv('../result/all-sensors-1.binetflow', single_file=True, index=False)
    print('storing data success')

    # reader = csv.reader(open('../result/all-sensors.binetflow'), delimiter=',')
    # sortedlist = sorted(reader, key=lambda row: row[1], reverse=True)

    # with open('final.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     header = ['StartTime','Dur','Proto','SrcAddr','Sport','Dir','DstAddr',
    #         'Dport','State','sTos','dTos','TotPkts','TotBytes','SrcBytes','Label',
    #         'activityLabel','bonetName','sensorId']

    #     # write the header
    #     writer.writerow(header)

    #     # write multiple rows
    #     writer.writerows(sortedlist)