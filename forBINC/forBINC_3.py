# Convert each of the ORF into putative proteins using
# the standard codontab.txt (input provided)
import re

desc = ''
total_seqeunce = ''
start = end = ''
proteins = dict()
minimum_length_of_ORF = 100
codontable = dict()

with open("gene.txt") as fin:
    for line in fin:
        if line.startswith(">"):
            desc = line
            continue
        total_seqeunce += line[:-1]

with open("codontab.txt") as codonf:
    for line in codonf:
        if line.startswith("Codons"):
            continue
        if "Stop" in line:
            data = re.match(r'([A-Z]{3})',line)
            codontable[data.group(1)] = "*"
            continue
        data = re.match(r'([A-Z]{3})\s+\([A-Z][a-z]{2}/([A-Z])\)', line)
        codontable[data.group(1)] = data.group(2)
print(codontable)

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
                protein = ''
                for i in range(0,len(orf),3):
                    protein += codontable[orf[i:i+3]]
                proteins[key] = protein
            start = ''

for item in proteins:
    print(item," : ",proteins[item],"\n")
