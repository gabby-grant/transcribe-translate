def transcribe_dna_to_rna(input_file, output_file):
    dna_to_rna = {
        "A": "A",
        "T": "U",
        "G": "G",
        "C": "C",
        "N": "N",
        "a": "A",
        "t": "U",
        "g": "G",
        "c": "C",
        "n": "N",
    }

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            current_sequence = []
            current_header = ""
            sequence_count = 0

            for line in infile:
                line = line.strip()
                if line.startswith(">"):
                    # If we have a previous sequence, transcribe and write it
                    if current_sequence:
                        dna_sequence = "".join(current_sequence)
                        rna_sequence = "".join(
                            [
                                dna_to_rna.get(nucleotide, "")
                                for nucleotide in dna_sequence
                            ]
                        )
                        outfile.write(f"{current_header}\n{rna_sequence}\n")
                        sequence_count += 1

                    # Start a new sequence
                    current_header = line
                    current_sequence = []
                else:
                    current_sequence.append(line.upper())

            # Transcribe and write the last sequence
            if current_sequence:
                dna_sequence = "".join(current_sequence)
                rna_sequence = "".join(
                    [dna_to_rna.get(nucleotide, "") for nucleotide in dna_sequence]
                )
                outfile.write(f"{current_header}\n{rna_sequence}\n")
                sequence_count += 1

        print(
            f"Transcription complete. {sequence_count} RNA sequences written to {output_file}"
        )

    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return

transcribe_dna_to_rna(input_file, output_file)
