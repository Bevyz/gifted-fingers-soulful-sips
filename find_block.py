file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find "massage-section"
idx = content.find('class="massage-section"')
print(content[idx-100:idx+2500])
