# Напишете програма, която чете от конзолата цяло число n и печата числата от 1 до 2n

count = int(input())

for number in range(0, count + 1):
    print(2 ** number)
