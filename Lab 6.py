# Capitalizes exons
dna = 'gctagctagctagcta'
exons = [(0,3),(5,8)]
annot = list(dna.lower())
for s,e in exons:    
  for i in range(s,e):        
    annot[i] = annot[i].upper()
print(''.join(annot))

# Counts the amount of nucleotides appear in sequence
dna = 'gctagctagctagcta'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}
print(counts)

# Reverse dna sequence
dna = 'gctagctagctagcta'
print(dna[::-1])
