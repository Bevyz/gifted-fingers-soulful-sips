import re

with open(r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find all drink-card-img alts and their src
for m in re.finditer(r'alt="([^"]+)" class="drink-card-img"', c):
    alt = m.group(1)
    start = max(0, m.start() - 500)
    snippet = c[start:m.start()]
    src_m = re.search(r'src="([^"]{0,120})', snippet)
    if src_m:
        src = src_m.group(1)
        if src.startswith('data:'):
            print(f'{alt} -> BASE64 ({src[5:30]}...)')
        else:
            print(f'{alt} -> {src}')
    else:
        print(f'{alt} -> NOT FOUND')
