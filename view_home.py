import sys
import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="home"')
if idx != -1:
    snippet = content[idx:idx+3500]
    # Remove base64 images so it prints cleanly
    snippet = re.sub(r'src=\"data:image/jpeg;base64,[^\"]+\"', 'src="..."', snippet)
    sys.stdout.buffer.write(snippet.encode('utf-8'))

