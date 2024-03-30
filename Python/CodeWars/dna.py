# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

#solved
def DNA_strand(dna):
    new_dna = ''
    #loop through dna symbols
    for char in dna:
        #add complementary dna symbol
        match char:
            case 'A':
                new_dna += 'T'
            case 'T':
                new_dna += 'A'
            case 'C':
                new_dna += 'G'
            case 'G':
                new_dna += 'C'
    return new_dna