# Find the ORFs on forward strand for the given
# nucleotide sequence using only start & end codon pattern.
desc = ''
total_seqeunce = ''
start = end = ''
ORFs = dict()
minimum_length_of_ORF = 100

with open("gene.txt") as fin:
    for line in fin:
        if line.startswith(">"):
            desc = line
            continue
        total_seqeunce += line[:-1]
# Finding for frame 1
for n in range(0,len(total_seqeunce), 3):
    codon = total_seqeunce[n:n+3]
    if codon == "ATG":
        start = n
    if codon in [ "TAA", "TGA", "TAG" ]:
        end = n
        if start:
            orf = total_seqeunce[start:end+3]
            if len(orf) > minimum_length_of_ORF:
                key = str(start)+" - "+str(end)
                ORFs[key] = orf
            start = ''

for item in ORFs:
    print(item," : ",ORFs[item],"\n")
