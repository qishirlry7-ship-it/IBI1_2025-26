# unit: amu
mass = {'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08}

def predict_protein_mass(x):
    protein_mass = 0 # It should be intitialized inside the def.
    for i in x:
        if i in mass.keys():
            protein_mass = protein_mass + mass[i]
        else:
            print('Amino acid ', i, ' has no recoreded mass.')
            return
    return 'Error: Amino acid ', i, ' has no recorded mass.'
print("""
Amino acid    Symbol
Glycine       G
Alanine       A
Serine        S
Proline       P
Valine        V
Threonine     T
Cysteine      C
Isoleucine    I
Leucine       L
Asparagine    N
Aspartic Acid D
Glutamine     Q
Lysine        K
Glutamic Acid E
Methionine    M
Histidine     H
Phenylalanine F
Arginine      R
Tyrosine      Y
Tryptophan    W""")
x = input('Please type a sequence of amino acid.')
result = predict_protein_mass(x)
print('The predicting protein mass is ', result)


