from rdkit.Chem import AllChem
from rdkit import Chem
from morfeus import read_xyz
import numpy as np
def gen_alk_bond_length_map(f,smi,smiles_match_idx_map):
    match_index = smiles_match_idx_map[smi]
    positions=read_xyz(f+'/xtbopt.xyz')[1]
    positions1=positions[match_index[0]]
    positions2=positions[match_index[1]]
    bond_length=np.linalg.norm(positions1-positions2)
    return bond_length
def gen_sub_bond_length_map(f,smi,smiles_match_idx_map):
    match_index = smiles_match_idx_map[smi]
    positions=read_xyz(f+'/xtbopt.xyz')[1]
    tmp_mol = AllChem.AddHs(Chem.MolFromSmiles(smi))
    atom = tmp_mol.GetAtomWithIdx(match_index[0])
    index2=list(set([x.GetIdx() for x in atom.GetNeighbors()])-set(list([match_index[1]])+list([match_index[4]])))
    positions1=positions[match_index[0]]
    positions2=positions[index2]
    bond_length1=np.linalg.norm(positions1-positions2)
    
    positions3=positions[match_index[0]]
    positions4=positions[match_index[1]]
    bond_length2=np.linalg.norm(positions3-positions4)
    
    positions5=positions[match_index[1]]
    positions6=positions[match_index[2]]
    bond_length3=np.linalg.norm(positions5-positions6)    
    
    positions7=positions[match_index[2]]
    positions8=positions[match_index[3]]
    bond_length4=np.linalg.norm(positions7-positions8)      

    positions9=positions[match_index[3]]
    positions10=positions[match_index[4]]
    bond_length5=np.linalg.norm(positions9-positions10)  

    positions11=positions[match_index[4]]
    positions12=positions[match_index[0]]
    bond_length6=np.linalg.norm(positions11-positions12)  ##

    positions13=positions[match_index[2]]
    positions14=positions[match_index[8]]
    bond_length7=np.linalg.norm(positions13-positions14)  

    positions15=positions[match_index[8]]
    positions16=positions[match_index[7]]
    bond_length8=np.linalg.norm(positions15-positions16)  

    positions17=positions[match_index[7]]
    positions18=positions[match_index[6]]
    bond_length9=np.linalg.norm(positions17-positions18) 

    positions19=positions[match_index[6]]
    positions20=positions[match_index[5]]
    bond_length10=np.linalg.norm(positions19-positions20) 

    positions21=positions[match_index[5]]
    positions22=positions[match_index[4]]
    bond_length11=np.linalg.norm(positions21-positions22)     
    
    
    return [bond_length1,bond_length2,bond_length3,bond_length4,bond_length5,bond_length6,
           bond_length7,bond_length8,bond_length9,bond_length10,bond_length11]
def gen_acid_bond_length_map(f,smi,smiles_match_idx_map):
    match_index = smiles_match_idx_map[smi]
    tmp_mol = AllChem.AddHs(Chem.MolFromSmiles(smi))
    atom = tmp_mol.GetAtomWithIdx(match_index[6])
    index2=list(set([x.GetIdx() for x in atom.GetNeighbors()])-set(list([match_index[5]])))
    positions=read_xyz(f+'/xtbopt.xyz')[1]
    positions1=positions[match_index[6]]
    positions2=positions[index2]
    bond_length1=np.linalg.norm(positions1-positions2)
    
    positions3=positions[match_index[14]]
    positions4=positions[match_index[15]]
    bond_length2=np.linalg.norm(positions3-positions4)
    
    positions5=positions[match_index[12]]
    positions6=positions[match_index[13]]
    bond_length3=np.linalg.norm(positions5-positions6)    
    
    positions7=positions[match_index[3]]
    positions8=positions[match_index[1]]
    bond_length4=np.linalg.norm(positions7-positions8)      

    positions9=positions[match_index[8]]
    positions10=positions[match_index[9]]
    bond_length5=np.linalg.norm(positions9-positions10)  

    positions11=positions[match_index[4]]
    positions12=positions[match_index[8]]
    bond_length6=np.linalg.norm(positions11-positions12)  

    positions13=positions[match_index[8]]
    positions14=positions[match_index[12]]
    bond_length7=np.linalg.norm(positions13-positions14)  

    positions15=positions[match_index[12]]
    positions16=positions[match_index[14]]
    bond_length8=np.linalg.norm(positions15-positions16)  

    positions17=positions[match_index[14]]
    positions18=positions[match_index[3]]
    bond_length9=np.linalg.norm(positions17-positions18) 

    positions19=positions[match_index[3]]
    positions20=positions[match_index[4]]
    bond_length10=np.linalg.norm(positions19-positions20) 

    positions21=positions[match_index[4]]
    positions22=positions[match_index[5]]
    bond_length11=np.linalg.norm(positions21-positions22)  
    
    positions23=positions[match_index[5]]
    positions24=positions[match_index[6]]
    bond_length12=np.linalg.norm(positions23-positions24)  

    positions25=positions[match_index[5]]
    positions26=positions[match_index[7]]
    bond_length13=np.linalg.norm(positions25-positions26)  
    return [bond_length1,bond_length2,bond_length3,bond_length4,bond_length5,bond_length6,
           bond_length7,bond_length8,bond_length9,bond_length10,bond_length11,bond_length12,bond_length13]
