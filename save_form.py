import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="booking"')
if idx != -1:
    snippet = content[idx:idx+5000]
    # Remove large base64 strings
    snippet = re.sub(r'src=\"data:image/jpeg;base64,[^\"]+\"', 'src="..."', snippet)
    with open('c:\\Users\\ikuda\\Downloads\\gifted-fingers-soulful-sips\\booking_snippet.txt', 'w', encoding='utf-8') as out:
        out.write(snippet)
