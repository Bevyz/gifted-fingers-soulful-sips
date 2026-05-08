import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Text 2 with Text 1
text_to_copy = "Professional, certified mobile massage therapists serving Lagos and surroundings. We come to your home, office, hotel, or event fully equipped."

# Text 2 pattern
pattern_2 = r'All sessions are fully mobile.*?ambience to your space\.'

match_2 = re.search(pattern_2, content, re.DOTALL)
if match_2:
    print("Found Text 2:", match_2.group(0))
    content = content.replace(match_2.group(0), text_to_copy)
else:
    print("Text 2 NOT found!")

# 2. Remove the hero tab (the gf-strip containing text_to_copy)
# We know the hero tab is a <div class="gf-strip"> that contains the text we just copied.
# Let's find the start of this <div class="gf-strip">
idx_text = content.find('"Healing your body, mind &amp; spirit."')
if idx_text != -1:
    # Go backwards to find the start of the div
    idx_start = content.rfind('<div class="gf-strip">', 0, idx_text)
    if idx_start != -1:
        # Now find the matching closing </div>. The gf-strip has an image, a gf-strip-text div, and an <a> tag.
        # Let's just find the end of the section by looking for the next </div> that closes the gf-strip.
        # Looking at previous output:
        # <div class="gf-strip">
        #   <img ... />
        #   <div class="gf-strip-text">...</div>
        #   <a ...>...</a>
        # </div>
        # Let's find the </a>
        idx_a_end = content.find('</a>', idx_text)
        if idx_a_end != -1:
            idx_div_end = content.find('</div>', idx_a_end)
            if idx_div_end != -1:
                idx_end = idx_div_end + 6
                print("Found gf-strip block to remove.")
                # print snippet to be sure
                # print(content[idx_start:idx_end])
                content = content[:idx_start] + content[idx_end:]
            else:
                print("Could not find closing </div>")
        else:
            print("Could not find closing </a>")
    else:
        print("Could not find <div class=\"gf-strip\">")
else:
    print("Could not find identifying text for the hero tab")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done.")

