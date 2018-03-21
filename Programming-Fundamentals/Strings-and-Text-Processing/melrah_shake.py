text = input()
pattern = input()

while pattern != '':
    f_index = text.find(pattern)
    l_index = text.rfind(pattern)
    has_matches = f_index != -1 and l_index != -1 and f_index != l_index
    if has_matches:
        print('Shaked it.')

        while has_matches:
            text = text[:f_index] + text[f_index + len(pattern):l_index] + text[l_index + len(pattern):]
            f_index = text.find(pattern)
            l_index = text.rfind(pattern)
            has_matches = f_index != -1 and l_index != -1 and f_index != l_index
    else:
        break
    pattern = pattern[:int(len(pattern) // 2)]
print(f'No shake.\n{text}')
