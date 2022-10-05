import pandas as pd
from utilities.common import *

def loadDataset(dataset, scenario):
  fileName = dataset[scenario] #load dataset
  raw_df=pd.read_csv(fileName)
  return raw_df

def loadSplitActivity(url, scenario, activity):
  filename = url+str(scenario)+'/'+activity+'.csv'
  print("Load: "+filename)
  df = pd.read_csv(filename)
  return df

def loadSensorsData(url, sensorId):
  filename = url+str(sensorId)+'.binetflow'
  print("Load: "+filename)
  df = pd.read_csv(filename)
  return df
