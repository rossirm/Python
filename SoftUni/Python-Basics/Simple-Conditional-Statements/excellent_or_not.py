# Да се напише конзолна програма, която въвежда оценка (десетично число)
# и отпечатва “Excellent!”, ако оценката е 5.50 или по-висока, или “Not excellent.”

grade = float(input())

if grade >= 5.5:
    print('Excellent!')
else:
    print('Not excellent.')
