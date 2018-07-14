# Read file and create complemntary strand seqeunce
seq1 = "ATGCatgc"
seq2 = "TACGtacg"
transtab = str.maketrans(seq1,seq2)
with open("gene.txt") as fin, open("gene_c.txt","w") as cout:
    for line in fin:
        if line.startswith(">"):
            line = line[:-1] + "[complemntary]" + line[-1]
            cout.write(line)
            continue
        cout.write(line.translate(transtab))
