# This code is part of a solution to the Rosalind challenge "String Slice".
# Rosalind Challenge: String Slice

first_start_pos = 91
first_end_pos = 97

sec_start_pos =130
sec_end_pos = 134

#example usage
txt ="n3jMKw5MIZjH0zOhgkx5c2fDJiLg1wufJ4kGXzJgscn8G1MWUUIvCQBlflpQBCPnrsoHibWvukySIuILF8XsxbCabhRReguluskzobiPobblsCXPnYzc21UHy7nwP3wBeDmelessjcnfRCpQNmB5Rg8s8ARErylC4NYG3MC7dr776F50a7gV0eRgfeNTiS9Q"

# Extracting and printing the specified slices from the string
print(f'{txt[first_start_pos:first_end_pos+1]} {txt[sec_start_pos:sec_end_pos+1]}')

