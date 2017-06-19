# Напишете програма, която въвежда число n и отпечатва числата от 1 до n през 3 (със стъпка 3)

count = int(input())

for number in range(1, count + 1, 3):
    print(number)
