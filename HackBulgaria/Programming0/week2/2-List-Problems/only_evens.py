__author__ = 'Боян'

n = input("Enter count of numbers: ")
nums = int(n)

even_numbers = []
evens_count = 0

counter = 1
while counter <= nums:
    number = input("Enter a number: ")
    number = int(number)

    if number % 2 == 0:
        even_numbers += [number]
        evens_count += 1

    counter += 1

print("There are {0} even numbers. They are: {1}".format(evens_count, even_numbers))