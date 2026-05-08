import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove `<div class="hero-right">...</div>`
idx_hero_right = content.find('<div class="hero-right">')
if idx_hero_right != -1:
    # Find the end of this div. We know it ends right before `<!-- Dual brand cards -->`
    idx_end_hero_right = content.find('<!-- Dual brand cards -->', idx_hero_right)
    if idx_end_hero_right != -1:
        # Actually, it's safer to find the closing div of hero-right. 
        # But looking at the HTML earlier:
        #       </div>
        #     </div>
        #
        #     <!-- Dual brand cards -->
        # We can just cut from `<div class="hero-right">` to just before `<!-- Dual brand cards -->`
        
        # Let's verify by just finding the exact end of hero-right div
        end_idx = content.rfind('</div>', idx_hero_right, idx_end_hero_right)
        end_idx = content.rfind('</div>', idx_hero_right, end_idx) + 6
        
        # We can just replace the whole hero-right block with nothing
        content = content[:idx_hero_right] + content[idx_end_hero_right:]
        print("Removed hero-right.")

# 2. Update .hero CSS to have 1 column
content = content.replace('grid-template-columns: 1fr 1fr;', 'grid-template-columns: 1fr;')
print("Updated .hero CSS.")

# 3. Add classes to dual-cards and append CSS for them
# Let's find the first dual-card (massage)
content = content.replace('<div class="dual-card" onclick="showSection(\'massage\')">', '<div class="dual-card massage-card" onclick="showSection(\'massage\')">')
# Second dual-card (drinks)
content = content.replace('<div class="dual-card" onclick="showSection(\'drinks\')">', '<div class="dual-card drinks-card" onclick="showSection(\'drinks\')">')

# Add the new CSS rules for massage-card and drinks-card
new_css = """
    .massage-card {
      background: linear-gradient(to right, var(--warm-white) 50%, transparent 100%), url('Assets/sweddish.jpg') right center / cover no-repeat;
    }
    .massage-card:hover {
      background: linear-gradient(to right, var(--sage-pale) 50%, transparent 100%), url('Assets/sweddish.jpg') right center / cover no-repeat;
    }

    .drinks-card {
      background: linear-gradient(to right, var(--warm-white) 50%, transparent 100%), url('Soulful sip assets/Phoenix blend.jpg') right center / cover no-repeat;
    }
    .drinks-card:hover {
      background: linear-gradient(to right, var(--sage-pale) 50%, transparent 100%), url('Soulful sip assets/Phoenix blend.jpg') right center / cover no-repeat;
    }
"""

# We can append this CSS to the end of the <style> block
idx_style_end = content.find('</style>')
if idx_style_end != -1:
    content = content[:idx_style_end] + new_css + content[idx_style_end:]
    print("Added dual-card CSS.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished updates.")
