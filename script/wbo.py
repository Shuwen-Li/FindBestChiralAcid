def gen_bond_wbo_map(file):
    with open(file,'r') as fr:
        lines = fr.readlines()
    bond_wbo_map = {(eval(line.strip().split()[0])-1,
                     eval(line.strip().split()[1])-1):eval(line.strip().split()[2]) for line in lines}
    return bond_wbo_map



