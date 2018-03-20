def check_palindrome(word):
    l = len(word)
    is_palindrome = True
    for c in range(l // 2):
        if word[c] != word[l - c -1]:
            is_palindrome = False
            break
    return is_palindrome


words = input().split(' ')
palindromes = {}
for w in words:
    if check_palindrome(w):
        palindromes[w] = True
print(', '.join(sorted(palindromes)))
