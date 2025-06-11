# Rosalind Challenge: Calculating GC Content
# This script calculates the GC content of DNA sequences provided in FASTA format.
def parse_fasta(fasta_string):
    fasta_dict = {}
    current_label = ''
    for line in fasta_string.strip().split('\n'):
        line = line.strip()
        if line.startswith('>'):
            current_label = line[1:]
            fasta_dict[current_label] = ''
        else:
            fasta_dict[current_label] += line
    return fasta_dict

# Function to calculate GC content of a DNA sequence
def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

# Function to find the sequence with the highest GC content
def highest_gc_content(fasta_string):
    fasta_dict = parse_fasta(fasta_string)
    max_gc_id = ''
    max_gc_value = 0.0

    for seq_id, sequence in fasta_dict.items():
        gc = gc_content(sequence)
        if gc > max_gc_value:
            max_gc_value = gc
            max_gc_id = seq_id

    return max_gc_id, round(max_gc_value, 6)

# Example input (can be replaced with input from a file or stdin)
fasta_input = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

# Run the function and print the result
result_id, result_gc = highest_gc_content(fasta_input)
print(result_id)
print(result_gc)
