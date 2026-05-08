import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

text_to_copy = "Professional, certified mobile massage therapists serving Lagos and surroundings. We come to your home, office, hotel, or event fully equipped."

# We want to replace Text 2 with text_to_copy.
# Let's find Text 2 exactly as it is in the HTML.
# It seems there's a special character  in the text. Let's find the exact string using regex.

match = re.search(r'All sessions are fully mobile.*?ambience to your space\.', content, re.DOTALL)
if match:
    text_2_exact = match.group(0)
    print("Found Text 2:", text_2_exact)
    content = content.replace(text_2_exact, text_to_copy)
else:
    print("Text 2 not found!")

# Now we want to remove the hero tab. Let's find where the gf-strip is that contains text_to_copy.
# The user wants to remove the hero tab. We need to find the <div class="gf-strip"> block.
# We'll use regex to find the block.
# Wait, there might be multiple gf-strip blocks. Let's find the one that contains "Healing your body, mind"
match_strip = re.search(r'<div class="gf-strip">.*?Healing your body, mind.*?</div>\s*</div>\s*(?:<!--)?', content, re.DOTALL)

# Better yet, let's write a python script that just looks for the index of <div class="gf-strip"> and matching closing tags.
