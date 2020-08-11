from gene import *



allele1 = gene(1,1,1)
allele2 = gene(1,1,1)

print(allele1.get_allele())
print(allele2.get_allele())

child = allele1.corssover(allele2)

print(child)

