"""Writen By: M. Aidiel Rachman Putra"""
"""Organization: Net-Centic Computing Laboratory | Institut Teknologi Sepuluh Nopember"""

from dataLoader import *
from extract import *
from simulate import *

if __name__ == "__main__":
#extract
    # datasetName = ctu
    # for i in range(1,14):
    #     selectedScenario = 'scenario'+str(i)
    #     df = loadDataset(datasetName, selectedScenario)
    #     splitActivity('ctu', df, i)
#simulation
    # simulation(3, 3,4,1,2,8,12,5)
#merging sensors
    mergingAllSensors()
