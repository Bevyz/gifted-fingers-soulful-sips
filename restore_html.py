import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's insert the missing HTML right before <div class="drinks-grid">
missing_html = """
      <!-- Brand note -->


      <p class="section-label">Our Signature Drinks</p>
      
      """

idx = content.find('<div class="drinks-grid">')
if idx != -1:
    new_content = content[:idx] + missing_html + content[idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Restored missing HTML.")
else:
    print("Could not find <div class=\"drinks-grid\">")
