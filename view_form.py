import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="booking"')
if idx != -1:
    snippet = content[idx:idx+5000]
    snippet = re.sub(r'src=\"data:image/jpeg;base64,[^\"]+\"', 'src="..."', snippet)
    print(snippet)

