import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the gallery
idx_start = content.find('<!-- Photo gallery -->')

# Find the end of the drinks-hero-gallery
# We know it's a div, and it ends before '<div class="drinks-grid">' or some other section.
# Let's find '<div class="drinks-grid">'
idx_end = content.find('<div class="drinks-grid">', idx_start)

if idx_start != -1 and idx_end != -1:
    print("Found section to remove:")
    # print the first and last 200 chars to confirm
    snippet = content[idx_start:idx_end]
    print(snippet[:200])
    print("...")
    print(snippet[-200:])
    
    # Let's remove it
    new_content = content[:idx_start] + content[idx_end:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed gallery successfully.")
else:
    print("Could not find start or end index.")
