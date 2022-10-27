import time
import os

from src.extract import *
from src.simulate import *
from utilities.common import *
from utilities.dataLoader import *

def banner():
    print("\n\n================================================================")
    print("======| Botnet Simultaneous Dataset Generator |=================")
    print("================================================================\n")
    print("Main Menu: ")
    for i, menu in enumerate(listMenu):
        print(str(i+1)+". "+menu)
    print("\n================================================================")

def executor(choose):
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
        print("++++++| Merging Sensors Process Success |++++++")
        print("...back to menu...")
    elif(int(choose) == len(listMenu)):
        print("++++++| Exit |++++++")
        exit()
    else:
        print("This Menu Does Not Exist, Please Try Another Input!")
        time.sleep(3) # adding 3 seconds time delay
        os.system("clear")

#menu
def mainMenu():
    banner()
    try:
        choose = input("Enter Menu: ")
    except EOFError as e:
        choose = '1'
    
    executor(choose)