# Define the input and output file names
input_file = "DNA_TO_RNA.fasta"  # Replace with your actual input RNA file name
output_file = "translated_proteins.fasta"  # Replace with your desired output file name

# Standard RNA codon table
rna_codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_rna(rna_sequence):
    """Translate RNA sequence to amino acid sequence"""
    protein = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if len(codon) == 3:
            amino_acid = rna_codon_table.get(codon, 'X')  # 'X' for unknown codons
            protein += amino_acid
    return protein
print(f"Starting translation process...")
print(f"Input file: {input_file}")
print(f"Output file: {output_file}")

# Read the input file and translate each sequence

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    current_sequence = []
    current_header = ""
    sequence_count = 0

    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            # If we have a previous sequence, translate and write it
            if current_sequence:
                rna_sequence = ''.join(current_sequence)
                protein_sequence = translate_rna(rna_sequence)
                outfile.write(f"{current_header}\n{protein_sequence}\n")
                sequence_count += 1
            
            # Start a new sequence
            current_header = line
            current_sequence = []
        else:
            current_sequence.append(line)

    # Translate and write the last sequence
    if current_sequence:
        rna_sequence = ''.join(current_sequence)
        protein_sequence = translate_rna(rna_sequence)
        outfile.write(f"{current_header}\n{protein_sequence}\n")
        sequence_count += 1

print(f"Translation complete. {sequence_count} protein sequences written to {output_file}")

# Verify file contents
with open(output_file, 'r') as check_file:
    content = check_file.read()
    print(f"Output file size: {len(content)} characters")
    print(f"First 100 characters of output file: {content[:100]}")
