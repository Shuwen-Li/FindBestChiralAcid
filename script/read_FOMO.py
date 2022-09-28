def read_FOMO(file):
    with open(file,'r',encoding='utf-8') as fr:
        lines = fr.readlines()
        for line in lines:
            if '(HOMO)' in line:
                homo = eval(line.strip().split()[2])
            elif '(LUMO)' in line:
                lumo = eval(line.strip().split()[1])
    return [homo,lumo]