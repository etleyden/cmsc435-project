
fin = open("proteins.txt")
fout = open("proteins.fasta", "w+")

proteins = fin.readlines()

for idx, protein in enumerate(proteins):
    fout.write(f">protein_{idx}\n{protein}")
