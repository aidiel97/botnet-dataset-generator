"""Writen By: M. Aidiel Rachman Putra"""
"""Organization: Net-Centic Computing Laboratory | Institut Teknologi Sepuluh Nopember"""

from dataLoader import *
from extract import *
from simulate import *
import time
import os

listMenu = [
    "Extract Source Dataset",
    "Start Simulation",
    "Merging All Sensors",
    "EXIT"
]

#extract
def extract():
    print("\n******************")
    print("Dataset Option: ")
    print("1. CTU-13")
    print("2. NCC")
    print("******************")
    datasetChoose = input("Select Dataset:")
    if(datasetChoose == "1"):
        datasetName = ctu
        stringDatasetName = 'ctu'
    else:
        datasetName = ncc
        stringDatasetName = 'ncc'
    for i in range(1,14):
        selectedScenario = 'scenario'+str(i)
        df = loadDataset(datasetName, selectedScenario)
        splitActivity(stringDatasetName, df, i)

#simulation
def simulate():
    simulation(1, 3,10,1,2,7,12,5)
    analytics(1)
    simulation(2, 10,11,1,2,9,6,13)
    analytics(2)
    simulation(3, 3,4,9,8,12,5,13)
    analytics(3)

#merging sensors
def merge():
    mergingAllSensors()
    # analytics('s-all')

#menu
def menu():
    print("\n\n================================================================")
    print("======| Botnet Simultaneous Dataset Generator |=================")
    print("================================================================\n")
    print("Main Menu: ")
    for i, menu in enumerate(listMenu):
        print(str(i+1)+". "+menu)
    print("\n================================================================")
    choose = input("Enter Menu: ")
    print("============| Processing Menu: "+choose+". "+listMenu[int(choose)-1]+" |========================\n")
    if(choose == "1"):
        extract()
        time.sleep(3) # adding 3 seconds time delay
        os.system("clear")
        print("++++++| Extraction Process Success |++++++")
        print("...back to menu...")
    elif(choose == "2"):
        simulate()
        time.sleep(3) # adding 3 seconds time delay
        os.system("clear")
        print("++++++| Simulation Process Success |++++++")
        print("...back to menu...")
    elif(choose == "3"):
        merge()
        time.sleep(3) # adding 3 seconds time delay
        os.system("clear")
        print("++++++| Extraction Process Success |++++++")
        print("...back to menu...")
    elif(int(choose) == len(listMenu)):
        print("++++++| Exit |++++++")
        exit()
    else:
        print("This Menu Does Not Exist, Please Try Another Input!")
        time.sleep(3) # adding 3 seconds time delay
        os.system("clear")

if __name__ == "__main__":
   while(True):
    menu()
