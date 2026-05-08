with open(r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if 'drink-card">' in line and '<img' in line:
        # Extract alt
        import re
        alt_m = re.search(r'alt="([^"]+)"', line)
        src_m = re.search(r'src="([^"]{0,80})', line)
        alt = alt_m.group(1) if alt_m else 'unknown'
        src = src_m.group(1) if src_m else 'unknown'
        if src.startswith('data:'):
            print(f'Line {i}: {alt} -> BASE64 ({src[5:35]}...)')
        else:
            print(f'Line {i}: {alt} -> {src}')
    elif 'drink-card">' in line:
        print(f'Line {i}: drink-card (no img on same line)')
