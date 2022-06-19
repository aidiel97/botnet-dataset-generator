"""Writen By: M. Aidiel Rachman Putra"""
"""Organization: Net-Centic Computing Laboratory | Institut Teknologi Sepuluh Nopember"""

from dataLoader import *
from extract import *
from simulate import *

if __name__ == "__main__":
    # datasetName = ctuLocal
    # for i in range(1,14):
    #     selectedScenario = 'scenario'+str(i)
    #     df = loadDataset(datasetName, selectedScenario)
    #     splitActivity(df, i)
    simulation(1)