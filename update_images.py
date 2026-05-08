import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Massage card image
content = content.replace("url('Assets/sweddish.jpg')", "url('Assets/Gifted fingers card.jpg')")

# Replace Drinks card image
content = content.replace("url('Soulful sip assets/Phoenix blend.jpg')", "url('Assets/Souldful sip card.jpg')")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images updated successfully.")
