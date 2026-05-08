import re
import sys

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="bk-service"')
if idx != -1:
    sys.stdout.buffer.write(b"--- HTML ---\n")
    sys.stdout.buffer.write(content[idx-300:idx+1500].encode('utf-8'))

idx_js = content.find('function sendToWhatsApp()')
if idx_js != -1:
    sys.stdout.buffer.write(b"\n--- JS ---\n")
    sys.stdout.buffer.write(content[idx_js:idx_js+1000].encode('utf-8'))
