def calculate_score(before, number, after):
    alphabet = ord('a') - 1
    score = 0

    b_pos = ord(before.lower()) - alphabet
    a_pos = ord(after.lower()) - alphabet

    if before.isupper():
        score += number / b_pos
    elif before.islower():
        score += number * b_pos

    if after.isupper():
        score -= a_pos
    elif after.islower():
        score += a_pos

    return score


words = input()
words = words.replace('\t', ' ')
words = filter(None, words.split(' '))
total = 0
for w in words:
    b = w[:1]
    a = w[-1:]
    d = w[1:-1]
    total += calculate_score(b, int(d), a)
print(f'{total:.2f}')
