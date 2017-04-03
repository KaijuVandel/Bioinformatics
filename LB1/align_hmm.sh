#!/bin/bash
hmmemit=/usr/bin/hmmemit
muscle=/usr/bin/muscle


hmm=$1
n=$2
outfile=$3


#Generate a set of n sequences from HMM
echo "Generate" $n "Sequences" >&2
$hmmemit -N $n -o $outfile".fasta" $hmm 

echo "Calculate the alignment" >&2
#Align sequences in outfile.fasta

$muscle -in $outfile".fasta" -out $outfile".aln" 2> /dev/null

#remove sequence file outfile.fasta

rm $outfile".fasta"
