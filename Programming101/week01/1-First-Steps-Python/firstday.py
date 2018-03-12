def sum_of_digits(n):
    number = abs(n)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10

    return total


print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))


def to_digits(n):
    return [d for d in str(n)]


print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))


def to_number(digits):
    return int(''.join([str(x) for x in digits]))


print(to_number([1, 2, 3]))
print(to_number([9, 9, 9, 9, 9]))
print(to_number([1, 2, 3, 0, 2, 3]))
print(to_number([21, 2, 33]))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


def fact_digits(n):
    total = 0
    for d in str(n):
        total += factorial(int(d))

    return total


print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))


def fibonacci(n):
    members = []
    first = 1
    second = 1
    third = first + second
    for i in range(n):
        members.append(first)

        first = second
        second = third
        third = first + second

    return members


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))


def fib_number(n):
    return ''.join([str(x) for x in fibonacci(n)])


print(fib_number(3))
print(fib_number(10))


def palindrome(obj):
    num = str(obj)
    end = len(num) - 1
    mid = end // 2 + 1

    is_palindrome = True
    for i in range(mid):
        if num[i] != num[end - i]:
            is_palindrome = False
            break

    return is_palindrome


print(palindrome(121))
print(palindrome('kapak'))
print(palindrome('baba'))


def count_vowels(text):
    vowels = 'aeiouyAEIOUY'
    total = 0
    for char in text:
        if char in vowels:
            total += 1

    return total


print(count_vowels('Python'))
print(count_vowels('Theistareykjarbunga'))
print(count_vowels('grrrrgh!'))
print(count_vowels('Github is the second best thing that happend to programmers, after the keyboard!'))
print(count_vowels('A nice day to code!'))


def count_consonants(text):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    total = 0
    for char in text:
        if char in consonants:
            total += 1

    return total


print(count_consonants('Python'))
print(count_consonants('Theistareykjarbunga'))
print(count_consonants('grrrrgh!'))
print(count_consonants('Github is the second best thing that happend to programmers, after the keyboard!'))
print(count_consonants('A nice day to code!'))


def char_histogram(string):
    histogram = {}
    for char in string:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1

    return histogram

print(char_histogram('Python!'))
print(char_histogram('AAAAaaa!!!'))