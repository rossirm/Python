__author__ = 'Боян'

n = input("Enter count of numbers: ")
nums = int(n)

min_num = 2147483647

counter = 1
while counter <= nums:
    number = input("Enter number: ")
    number = int(number)
    if number <= min_num:
        min_num = number
    counter += 1

print(min_num)