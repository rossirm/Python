__author__ = 'Боян'

n = input("Enter count of numbers: ")
nums = int(n)

total = 0

counter = 1
while counter <= nums:
    number = input("Enter number: ")
    number = int(number)
    total += number
    counter += 1

print(total / nums)