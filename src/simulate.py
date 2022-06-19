# unique scenario: 1,3,4,6,7,8,9,10,12,13
# normal activiyy source: 3,8,
from datetime import datetime, timedelta
from dataLoader import *
urlExtractData = '../extract/ctu/'

def simulation(totalHours):
    # now = datetime.now()
    # print(now.strftime("%Y/%m/%d %H:%M:%S"))
    # totalSeconds = totalHours*3600
    # for i in range(totalSeconds):
    #     print((now+timedelta(seconds=i)).strftime("%Y/%m/%d %H:%M:%S"))
    # bot_df1 = loadSplitActivity(urlExtractData, 1, 'botnet')
    bot_df3 = loadSplitActivity(urlExtractData, 3, 'botnet')
    # bot_df4 = loadSplitActivity(urlExtractData, 4, 'botnet')
    # bot_df6 = loadSplitActivity(urlExtractData, 6, 'botnet')
    # bot_df7 = loadSplitActivity(urlExtractData, 7, 'botnet')
    # bot_df8 = loadSplitActivity(urlExtractData, 8, 'botnet')
    bot_df9 = loadSplitActivity(urlExtractData, 9, 'botnet')
    bot_df10 = loadSplitActivity(urlExtractData, 10, 'botnet')
    bot_df12 = loadSplitActivity(urlExtractData, 12, 'botnet')
    bot_df13 = loadSplitActivity(urlExtractData, 13, 'botnet')

    normal_df3 = loadSplitActivity(urlExtractData, 3, 'normal')
    normal_df8 = loadSplitActivity(urlExtractData, 8, 'normal')
    print('datasets loaded')

    #concat
    df_result = pd.concat([bot_df3,bot_df9,bot_df10,bot_df12,bot_df13,normal_df3])
    # df_result = pd.concat([bot_df1,bot_df3,bot_df4,bot_df7,bot_df8,bot_df9,bot_df10,bot_df12,bot_df13,normal_df3,normal_df8])
    print('dataset concated')

    #sort by StartTime
    df_result.sort_values(by='syntheticTime', inplace=True)
    df_result.reset_index(drop=True, inplace=True)
    print('sorting success')

    df_result['StartTime'] = df_result['syntheticTime']
    df_result.to_csv('../result/simultaneous.csv', index=False)

    print('storing data success')