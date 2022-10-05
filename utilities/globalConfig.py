import os
from dotenv import load_dotenv

load_dotenv()

DATASET_LOCATION = os.getenv('DATASET_LOCATION')
URL_EXTRACTED_DATA = os.getenv('URL_EXTRACTED_DATA')
CTU_DIR = os.getenv('CTU_DIR')
NCC_DIR = os.getenv('NCC_DIR')
NCC2_DIR = os.getenv('NCC2_DIR')

SYNTHETIC_DATE = os.getenv('SYNTHETIC_DATE')
SYNTHETIC_TIME = os.getenv('SYNTHETIC_TIME')
LIMIT_TIME = os.getenv('LIMIT_TIME')