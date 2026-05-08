import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all img tags in the document and print their classes or parent classes
img_tags = re.findall(r'<img[^>]+>', content)
for img in img_tags:
    if 'drink-card-img' not in img and 'brand-logo' not in img:
        print(img[:100] + '...')

