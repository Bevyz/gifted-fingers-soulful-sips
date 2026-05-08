import os

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content.replace("Cellular Hydration", "Serotonin Sips")
new_content = new_content.replace("cellular hydration", "serotonin sips")

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replacements made.")
else:
    print("No occurrences found.")
