#!/bin/bash
while read -r header; do
    read -r sequence
    echo -e "$header\n$sequence"
    echo -e "$header\n$sequence" > temp.fasta
    psiblast -query temp.fasta -db swissprot -num_iterations 3 -out_ascii_pssm "${header:1}.pssm"
done < proteins.fasta
rm temp.fasta

