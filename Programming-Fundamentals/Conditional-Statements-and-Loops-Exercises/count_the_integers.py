count = 0
while True:
    try:
        int(input())
        count += 1
    except Exception:
        break

print(count)
