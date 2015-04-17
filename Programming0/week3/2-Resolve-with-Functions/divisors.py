__author__ = 'Боян'


def divisors(number):
    result = []

    counter = 1
    while counter < number:
        if number % counter == 0:
            result += [counter]
        counter += 1
    return result


n = input("Enter a number")
divs = divisors(int(n))

print("The divisors of {0} are :".format(n))
for divisor in divs:
    print(divisor)