match_idx={}
for smi in smi_set:
    if smi in re_1_smi_set:
        mol = AllChem.AddHs(Chem.MolFromSmiles(smi))
        match_idx[smi]=mol.GetSubstructMatch(Chem.MolFromSmiles('O=CC(C=CC=C1)=C1C2=CC=CC=C2'))
