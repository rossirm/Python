# да се напише конзолна програма, която въвежда оценка (десетично число)
# и отпечатва “Excellent!”, ако оценката е 5.50 или по-висока,
# “Very bad!”, ако е по-ниска от 3
# или “Not excellent.” в противен случай.

grade = float(input())

if 5.5 <= grade:
    print('Excellent!')
elif 5.5 > grade >= 3:
    print('Not excellent.')
else:
    print('Very bad!')
