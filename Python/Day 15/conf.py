import os

ABS_PATH = os.path.abspath(__file__)  #this gives filename where directly conf.py is
BASE_DIR = os.path.dirname(ABS_PATH) #give dir it lives in
DATA_DIR = os.path.join(BASE_DIR, "data") #paths
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')