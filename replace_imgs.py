"""
Replace base64 img src attributes in all remaining drink-card elements.
Does multiple passes to avoid position-shift bugs.
"""

import re

HTML_FILE = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

# Maps alt text -> local image path
ALT_TO_PATH = {
    'Caribbean Crush': 'Soulful sip assets/Carribean crush.jpg',
    'Bulk &amp; Butts Smoothie': 'Soulful sip assets/Bulk and Butts.jpg',
    'Cellular Hydration': 'Soulful sip assets/serotonin sips.jpg',
    'Cocoa Serenade': 'Soulful sip assets/Cocoa Serenade.jpg',
    'Clean House': 'Soulful sip assets/Clean House.jpg',
    'Greens in the Yard': 'Soulful sip assets/Green in the yard.jpg',
    'VitalHeal-C': 'Soulful sip assets/VitaHeal-C.jpg',
    'Phoenix Blend': 'Soulful sip assets/Phoenix blend.jpg',
    'Milky Temptation': 'Soulful sip assets/Milky Temptation.jpg',
    'Fruitilicious': 'Soulful sip assets/Fruitilicious.jpg',
    'Parfait': 'Soulful sip assets/Parfait.jpg',
    'Spice of Her': 'Soulful sip assets/Spice of her.jpg',
}

print(f"Reading {HTML_FILE}...")
with open(HTML_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)
print(f"File size: {original_size:,} bytes")

total_replacements = 0

# Process each alt text separately - do a fresh scan each time
for alt_text, new_src in ALT_TO_PATH.items():
    # Find this img by its alt attribute - look for the sequence:
    # src="..." alt="ALT_TEXT" class="drink-card-img"
    # The src value ends with " and alt immediately follows whitespace
    
    # Pattern: find alt="ALT" and then backtrack to find the src
    alt_marker = f'alt="{alt_text}" class="drink-card-img"'
    alt_pos = content.find(alt_marker)
    
    if alt_pos == -1:
        print(f"  '{alt_text}': alt marker not found, skipping")
        continue
    
    # From alt_pos, look backwards for src="
    search_region_start = max(0, alt_pos - 2000000)  # look up to 2MB back (base64 can be large)
    region = content[search_region_start:alt_pos]
    
    # Find the last src=" in this region
    src_eq_offset = region.rfind('src="')
    if src_eq_offset == -1:
        print(f"  '{alt_text}': src attribute not found before alt, skipping")
        continue
    
    src_eq_abs = search_region_start + src_eq_offset
    src_value_start = src_eq_abs + 5  # after src="
    src_value_end = content.find('"', src_value_start)
    
    old_src = content[src_value_start:src_value_end]
    
    if old_src == new_src:
        print(f"  '{alt_text}': already using local path, skipping")
        continue
    
    if not old_src.startswith('data:'):
        print(f"  '{alt_text}': src is not base64 ({old_src[:50]}), skipping")
        continue
    
    # Replace the src value
    content = content[:src_value_start] + new_src + content[src_value_end:]
    print(f"  '{alt_text}': replaced {len(old_src):,} base64 chars -> '{new_src}'")
    total_replacements += 1

print(f"\nTotal replacements: {total_replacements}")
print(f"New file size: {len(content):,} bytes")
print(f"Size reduction: {original_size - len(content):,} bytes ({(original_size - len(content)) / original_size * 100:.1f}%)")

print(f"Writing back to {HTML_FILE}...")
with open(HTML_FILE, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
