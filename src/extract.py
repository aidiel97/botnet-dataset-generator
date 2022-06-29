import pandas as pd

botName = {
    1:'neris',
    2:'neris',
    3: 'rbot',
    4: 'rbot',
    5: 'virut',
    6: 'menti',
    7: 'sogou',
    8: 'murlo',
    9: 'neris',
    10: 'rbot',
    11: 'rbot',
    12: 'nsis.ay',
    13: 'virut'
}

def splitActivity(datasetName, df, scenario):
    #create new label for bot prediciton(1/0)
    df['activityLabel'] = df['Label'].str.contains('botnet', case=False, regex=True).astype(int)
    syntheticTime="2022/06/18 00:00:00.000"

    #create new dataframe only botnet
    botnet = df['activityLabel'] == 1
    botnet_df = df[botnet]
    botnet_df.reset_index(drop=True, inplace=True)
    botnet_df['bonetName'] = botName[scenario]
    botnet_df['diff'] = pd.to_datetime(botnet_df['StartTime']) - pd.to_datetime(botnet_df['StartTime'][0])
    botnet_df['syntheticTime'] = pd.to_datetime(syntheticTime) + pd.to_timedelta(botnet_df['diff'], unit='s')

    #create new dataframe only normal
    normal = df['activityLabel'] == 0
    normal_df = df[normal]
    normal_df.reset_index(drop=True, inplace=True)
    normal_df['bonetName'] = '-'
    normal_df['diff'] = pd.to_datetime(normal_df['StartTime']) - pd.to_datetime(normal_df['StartTime'][0])
    normal_df['syntheticTime'] = pd.to_datetime(syntheticTime) + pd.to_timedelta(normal_df['diff'], unit='s')

    #export botnet to csv
    botnet_df.to_csv('../extract/'+datasetName+'/'+str(scenario)+'/botnet.csv', index=False)
    print('extract botnet scenario '+str(scenario)+' success!')

    #export normal to csv
    normal_df.to_csv('../extract/'+datasetName+'/'+str(scenario)+'/normal.csv', index=False)
    print('extract normal scenario '+str(scenario)+' success!')
