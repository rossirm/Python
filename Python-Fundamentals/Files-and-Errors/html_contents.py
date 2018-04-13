title = ''
tags = []

line = input()
while line != 'exit':
    tag_name, content = line.split(' ')
    if tag_name == 'title':
        title = content
    else:
        tag = f'\t<{tag_name}>{content}</{tag_name}>'
        tags.append(tag)

    line = input()

body_content = '\n'.join([t for t in tags])

html = f'''<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
{body_content}
</body>
</html>
'''

with open('index.html', 'w')as i:
    i.write(html)
