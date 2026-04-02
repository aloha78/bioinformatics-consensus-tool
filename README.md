# bioinformatics-consensus-tool

This code helps you to create consensus sequence from FASTA files.

TOOLS:  pandas, numpy, Tkinter

# How it works:

1. Load a FASTA file with protein sequences
2. The program:
  Parses sequences
  Builds an alignment matrix
  Calculates amino acid frequencies per position
3. Constructs a consensus sequence by selecting the most frequent amino acid
4. Identifies conserved regions (continuous segments with ≥90% frequency)
5. Saves results into consensus.fasta
