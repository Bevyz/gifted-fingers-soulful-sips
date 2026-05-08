import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("--- CSS for section-label ---")
css_match = re.search(r'\.section-label\s*{[^}]*}', content)
if css_match:
    print(css_match.group(0))

print("\n--- Booking Form HTML ---")
idx = content.find('id="booking"')
if idx != -1:
    print(content[idx:idx+2500])
