import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <select> to have 'multiple' and some inline style to ensure it displays properly
# The original is: <select id="bk-service">
content = content.replace('<select id="bk-service">', '<select id="bk-service" multiple style="height: auto; min-height: 120px;">')

# 2. Update sendToWhatsApp JavaScript
# Original:
# const service = document.getElementById('bk-service').value || 'Not selected';
# Replacement:
# const serviceSelect = document.getElementById('bk-service');
# const selectedOptions = Array.from(serviceSelect.selectedOptions).map(opt => opt.value || opt.text);
# const service = selectedOptions.length > 0 ? selectedOptions.join(', ') : 'Not selected';
old_js = "const service = document.getElementById('bk-service').value || 'Not selected';"
new_js = """const serviceSelect = document.getElementById('bk-service');
      const selectedOptions = Array.from(serviceSelect.selectedOptions).map(opt => opt.value || opt.text);
      const service = selectedOptions.length > 0 ? selectedOptions.join(', ') : 'Not selected';"""
content = content.replace(old_js, new_js)

# 3. Update .section-label CSS
# Original:
# .section-label {
#       font-size: .7rem;
#       letter-spacing: .3em;
#       text-transform: uppercase;
#       color: var(--clay);
#       margin-bottom: 3rem;
#       text-align: center
#     }
old_css = """.section-label {
      font-size: .7rem;
      letter-spacing: .3em;
      text-transform: uppercase;
      color: var(--clay);
      margin-bottom: 3rem;
      text-align: center
    }"""
new_css = """.section-label {
      font-size: 1.2rem;
      font-weight: 600;
      letter-spacing: .3em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 3rem;
      text-align: center
    }"""
content = content.replace(old_css, new_css)

# Wait, let's make sure the CSS replacement matched something. If not, I'll use regex.
if old_css not in content:
    # use regex
    pattern = r'\.section-label\s*\{[^}]*\}'
    content = re.sub(pattern, new_css, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied.")
