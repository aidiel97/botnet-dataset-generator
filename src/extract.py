import warnings
warnings.filterwarnings('ignore')
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
    print("\n====================Extracting "+datasetName+" Scenario"+str(scenario)+" START==")
    #sorting & remove index
    df.sort_values(by='StartTime', inplace=True)
    df.reset_index(drop=True, inplace=True)

    #create new label for bot prediciton(1/0)
    df['ActivityLabel'] = df['Label'].str.contains('botnet', case=False, regex=True).astype(int)
    syntheticTime="2022/07/07 09:00:00.000"
    limitTime="2022/07/07 17:00:01.000"

    #create new dataframe only botnet
    botnet = df['ActivityLabel'] == 1
    botnet_df = df[botnet]
    botnet_df.reset_index(drop=True, inplace=True)
    botnet_df['BotnetName'] = botName[scenario]
    botnet_df['Diff'] = pd.to_datetime(botnet_df['StartTime'].str[:19]) - pd.to_datetime(botnet_df['StartTime'].str[:19][0])
    botnet_df['SyntheticTime'] = pd.to_datetime(syntheticTime) + pd.to_timedelta(botnet_df['Diff'], unit='s')
    botnet_df['Limit'] = pd.to_datetime(botnet_df['SyntheticTime']) < pd.to_datetime(limitTime)
    
    limitedbot = botnet_df['Limit'] == True
    botnet_df_limited = botnet_df[limitedbot]

    #create new dataframe only normal
    normal = df['ActivityLabel'] == 0
    normal_df = df[normal]
    normal_df.reset_index(drop=True, inplace=True)
    normal_df['BotnetName'] = '-'
    normal_df['Diff'] = pd.to_datetime(normal_df['StartTime'].str[:19]) - pd.to_datetime(normal_df['StartTime'].str[:19][0])
    normal_df['SyntheticTime'] = pd.to_datetime(syntheticTime) + pd.to_timedelta(normal_df['Diff'], unit='s')
    normal_df['Limit'] = pd.to_datetime(normal_df['SyntheticTime']) < pd.to_datetime(limitTime)

    limitedNormal = normal_df['Limit'] == True
    normal_df_limited = normal_df[limitedNormal]

    #export botnet to csv
    botnet_df_limited.to_csv('../extract/'+datasetName+'/'+str(scenario)+'/botnet.csv', index=False)
    print('extract botnet scenario '+str(scenario)+' success!')

    #export normal to csv
    normal_df_limited.to_csv('../extract/'+datasetName+'/'+str(scenario)+'/normal.csv', index=False)
    print('extract normal scenario '+str(scenario)+' success!')

    print("====================Extracting "+datasetName+" Scenario"+str(scenario)+" END==")