__author__ = 'Боян'


def is_string_palindrome(string):
    normalized = ""
    for char in string:
        if char == "," or char == "." or char == "!" or char == "?" or char == " ":
            continue
        else:
            normalized += char

    length = len(normalized)
    normalized = normalized.lower()

    is_palindrome = True
    for c in range(0, length // 2):
        if normalized[c] != normalized[length - 1 - c]:
            is_palindrome = False
            break
    return is_palindrome


print(is_string_palindrome("Az obi4am ma4 i boza"))
print(is_string_palindrome("A Toyota!"))
print(is_string_palindrome("bozaaa"))
print(is_string_palindrome("    kapak!   "))