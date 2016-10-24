__author__ = 'Боян'

n = input("Enter count of numbers: ")
nums = int(n)

max_num = -2147483647

counter = 1
while counter <= nums:
    number = input("Enter number: ")
    number = int(number)

    if number >= max_num:
        max_num = number

    counter += 1

print("The max is: {0} ".format(max_num))