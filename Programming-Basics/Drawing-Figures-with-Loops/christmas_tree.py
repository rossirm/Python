count = int(input())

leaf = '*'
space = ' '
new_line = '\n'
stem = " | "

tree = ''
for i in range(count + 1):
    left_branch = space * (count - i) + leaf * i
    right_branch = leaf * i
    tree += left_branch + stem + right_branch + new_line

print(tree)
