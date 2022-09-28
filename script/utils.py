def maxminscale(array):
    return (array - array.min(axis=0))/(array.max(axis=0)-array.min(axis=0))

def ddG2ee(ddG):
    T=25+273.15
    ddG = ddG*1000*4.18
    ee = (1-np.exp(ddG/(8.314*T)))/(1+np.exp(ddG/(8.314*T)))
    return np.abs(ee)




