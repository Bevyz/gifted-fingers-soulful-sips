import sys

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

sys.stdout.buffer.write(b"--- BOOKING SECTION ---\n")
idx = content.find('id="booking"')
if idx != -1:
    sys.stdout.buffer.write(content[idx-100:idx+1500].encode('utf-8'))

sys.stdout.buffer.write(b"\n\n--- OUR TREATMENTS ---\n")
idx2 = content.lower().find('our treatments')
if idx2 != -1:
    sys.stdout.buffer.write(content[idx2-200:idx2+200].encode('utf-8'))
    
sys.stdout.buffer.write(b"\n\n--- OUR SIGNATURE DRINKS ---\n")
idx3 = content.lower().find('our signature drink')
if idx3 != -1:
    sys.stdout.buffer.write(content[idx3-200:idx3+200].encode('utf-8'))
