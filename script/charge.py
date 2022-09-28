import numpy as np
def read_charge(file):
    with open(file,'r') as fr:
        lines = fr.readlines()
    charges = np.array([eval(line.strip()) for line in lines])
    return charges