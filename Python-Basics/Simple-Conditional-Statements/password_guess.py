# Да се напише програма, която въвежда парола (един ред с произволен текст)
# и проверява дали въведеното съвпада с фразата “s3cr3t!P@ssw0rd”.
# При съвпадение да се изведе “Welcome”.
# При несъвпадение да се изведе “Wrong password!”.

user_input = input()

password = 's3cr3t!P@ssw0rd'
if user_input == password:
    print('Welcome')
else:
    print('Wrong password!')
