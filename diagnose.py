"""
Investigate actual drink-card structure - search beyond base64 data.
"""

HTML_FILE = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Find all drink-card positions
positions = []
start = 0
while True:
    pos = content.find('<div class="drink-card">', start)
    if pos == -1:
        break
    positions.append(pos)
    start = pos + 1

print(f"Found {len(positions)} drink-card divs")

for i, pos in enumerate(positions):
    # Find closing > of the img tag - look for alt= which should be after the src="" closing quote
    # The src="" attribute has base64 data, then closes with "
    # Then we have alt=
    
    # Find the end of the src attribute value (look for '" alt=' pattern)
    search_start = pos
    # Find the img tag opening
    img_start = content.find('<img', pos)
    if img_start == -1:
        print(f"Card {i+1}: No img tag found!")
        continue
    
    # Find src=" 
    src_eq = content.find('src="', img_start)
    if src_eq == -1:
        print(f"Card {i+1}: No src= found!")
        continue
    
    src_value_start = src_eq + 5  # after src="
    
    # Find the closing " of src value - look for '" alt=' 
    # We need to find the next " that is followed by whitespace+alt=
    # Since the base64 data doesn't contain quotes, just find the next "
    src_value_end = content.find('"', src_value_start)
    
    src_value = content[src_value_start:src_value_end]
    
    # Now find alt after src
    after_src = content[src_value_end:src_value_end+200]
    alt_match = re.search(r'alt="([^"]+)"', after_src)
    
    if src_value.startswith('data:'):
        src_display = f"[BASE64 {len(src_value)} chars]"
    else:
        src_display = src_value
    
    print(f"Card {i+1}: src={src_display}")
    if alt_match:
        print(f"         alt='{alt_match.group(1)}'")
    else:
        # Print what comes after src to debug
        print(f"         after_src: {repr(after_src[:100])}")
    print()
