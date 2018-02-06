text = input()
jump = int(input())
char = 'p'

result = ''
has_match = False
i = 0
while i < len(text):
    if text[i] == char:
        has_match = True
        end_index = i + jump + 1
        if end_index > len(text):
            end_index = len(text)

        result += f'{text[i:end_index]}\n'
        i += jump

    i += 1

if not has_match:
    result = 'no'
print(result)
