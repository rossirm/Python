# Напишете програма, която отпечатва всички букви от латинската азбука: a, b, c, …, z.

for code in range(ord('a'), ord('z') + 1):
    print(chr(code))
