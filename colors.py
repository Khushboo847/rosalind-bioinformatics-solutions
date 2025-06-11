# A simple script to colorize DNA sequences in the terminal.
import random

def colorize(seq):
    bcolors = {
        "A": "\033[92m",  # Green
        "C": "\033[94m",  # Blue
        "G": "\033[93m",  # Yellow
        "T": "\033[91m",  # Red
        "U": "\033[91m",  # Red (for RNA)
        "reset": "\033[0m"  # Reset
    }
    
    colored_seq = ""
    for nuc in seq:
        colored_seq += bcolors.get(nuc, bcolors["reset"]) + nuc
    colored_seq += bcolors["reset"]  # Reset color at the end
    return colored_seq



# Generate a random DNA sequence
nucleotides = ["A", "T", "C", "G"]
random_sequence = ''.join(random.choice(nucleotides) for nuc in range(50))

# Print a randomly generated sequence
random_string = random_sequence
print(f'\nRandom Sequence: {colorize(random_string)}\n')
