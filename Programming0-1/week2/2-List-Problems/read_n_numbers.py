__author__ = 'Боян'

n = input("Enter count of numbers: ")
nums = int(n)

count = 1
numbers = []

while count <= nums:
    number = input("Enter a number: ")
    number = int(number)
    numbers += [number]
    count += 1

print(numbers)