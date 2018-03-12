def find_sequence(seq):
    if not seq:
        return seq

    length = [None] * len(seq)
    prev = [None] * len(seq)
    max_length = 0
    last_index = -1

    for i in range(len(seq)):
        length[i] = 1
        prev[i] = 1

        for j in range(i):
            if seq[j] < seq[i] and length[j] >= length[i]:
                length[i] = length[j] + 1
                prev[i] = j
        if length[i] > max_length:
            max_length = length[i]
            last_index = i

    longest = []
    for s in range(max_length):
        longest.append(seq[last_index])
        last_index = prev[last_index]
    return longest[::-1]


sequence = input().split(' ')
result = find_sequence(sequence)
print(' '.join(result))
