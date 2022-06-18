def splitActivity(df, scenario):
    #create new label for bot prediciton(1/0)
    df['activityLabel'] = df['Label'].str.contains('botnet', case=False, regex=True).astype(int)
    
    #create new dataframe only botnet
    botnet = df['activityLabel'] == 1
    botnet_df = df[botnet]

    #create new dataframe only normal
    normal = df['activityLabel'] == 0
    normal_df = df[normal]

    #export botnet to csv
    botnet_df.to_csv('../extract/ctu/'+str(scenario)+'/botnet.csv', index=False)
    print('extract botnet scenario '+str(scenario)+' success!')

    #export normal to csv
    normal_df.to_csv('../extract/ctu/'+str(scenario)+'/normal.csv', index=False)
    print('extract normal scenario '+str(scenario)+' success!')
