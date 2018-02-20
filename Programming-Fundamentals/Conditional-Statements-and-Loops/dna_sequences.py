match = int(input())

nucleotides = {1: 'A', 2: 'C', 3: 'G', 4: 'T'}
count = 0
sequences = ''
for a in nucleotides:
    for b in nucleotides:
        for c in nucleotides:
            is_valid = a + b + c >= match
            if is_valid:
                sequences += f'O{nucleotides[a]}{nucleotides[b]}{nucleotides[c]}O'
            else:
                sequences += f'X{nucleotides[a]}{nucleotides[b]}{nucleotides[c]}X'
            count += 1
            if count % 4 == 0:
                sequences += '\n'
            else:
                sequences += ' '

print(sequences)
