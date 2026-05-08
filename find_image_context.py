import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find all positions of '<div class="drinks-gallery">' or something similar
# Since we don't know the exact class, let's just find the text "VitalHeal-C" and look around it, but I already did and only found the drink card.
# Wait, maybe the text "VitalHeal-C" in the image is literally IN THE IMAGE! It's a base64 image!
# Let's search for "drinks-gallery" or "gallery" classes in the document.
matches = re.finditer(r'<div[^>]*class=\"[^\"]*gallery[^\"]*\"[^>]*>', content, re.IGNORECASE)
for match in matches:
    start = match.start()
    print("Found gallery at:", start)
    print(content[start:start+200])

# Let's also look for a div containing exactly three base64 images.
# We can find blocks with multiple base64 images close together.
# Let's just find all <img src="data:image/jpeg;base64... tags and print their contexts.
img_matches = list(re.finditer(r'<img[^>]+src=\"data:image/jpeg;base64,[^\"]+\"[^>]*>', content))

for i, match in enumerate(img_matches):
    # Only print if it doesn't have brand-logo
    if 'brand-logo' not in match.group(0):
        start = max(0, match.start() - 200)
        print(f"\n--- Image {i} Context ---")
        # remove base64 string to keep output clean
        snippet = content[start:match.end()+200]
        snippet = re.sub(r'src=\"data:image/jpeg;base64,[^\"]+\"', 'src="..."', snippet)
        print(snippet[:400])

