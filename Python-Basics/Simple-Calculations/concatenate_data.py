# Напишете Python програма, която прочита от конзолата име, фамилия, възраст и град и печата съобщение от следния вид:
# “You are <firstName> <lastName>, a <age>-years old person from <town>”.

first_name = input()
last_name = input()
age = int(input())
town = input()

print('You are {0} {1}, a {2}-years old person from {3}.'.format(first_name, last_name, age, town))
