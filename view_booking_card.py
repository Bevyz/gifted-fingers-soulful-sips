import re
import sys

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<div class="booking-card">')
if idx != -1:
    idx_end = content.find('<footer', idx)
    snippet = content[idx:idx_end]
    snippet = re.sub(r'<img[^>]+>', '[IMG]', snippet)
    sys.stdout.buffer.write(snippet.encode('utf-8'))

