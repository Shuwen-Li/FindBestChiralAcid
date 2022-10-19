# FindBestChiralAcid
This is a repository for paper "Data-driven design of new chiral carboxylic acid for asymmetric cobalt catalyzed C–H alkylation".

# Introduction
In light of the critical knowledge transfer for catalyst development, we envision that the digitalization of the knowledge transfer process can serve as a new data-driven strategy for catalyst design. This requires the ML model to capture the differences between the given transformation and the target reaction, so that the available statistics of the given transformation can serve as a knowledge source and guide the target design. Herein we report the development of a data-driven transfer learning workflow to achieve the ML prediction of catalytic performance using related synthetic data. Demonstrated in the discovery of new CCA catalyst, our ML model provided a powerful CCA prediction that realized the challenging asymmetric cobalt-catalyzed C–H alkylation of indoles. The ML-designed CCA catalyst enabled the target transformation that can simultaneously control both the C-centered and the C–N axial chirality, providing the atropisomeric indoles with excellent diastereo- and enantioselectivities. This work offered a paradigm-shifting tool for the discovery of molecular catalyst, which will serve as a powerful data engine to support the innovation of catalysis science.


# Packages requirements
In order to run Jupyter Notebook involved in this repository, several third-party python packages are required. The versions of these packages in our station are listed below.
```
matplotlib = 3.4.2
morfeus = 0.5.5 
numpy = 1.22.4  
pandas = 1.3.3 
rdkit = 2022.03.2   
scipy = 1.4.1 
seaborn = 0.11.1 
sklearn = 0.23.2  
xgboost = 1.3.3 
```

# Demo & Instructions for use
Notebook 1 demonstrates how to generate descriptors.

Notebook 2 demonstrates the process of model selection.

Notebook 3 demonstrates the process of prediction.

Notebook 4 demonstrates the baseline of prediction.
# How to cite
The paper is under review.
# Contact with us
Email: hxchem@zju.edu.cn; shuwen_li@zju.edu.cn
