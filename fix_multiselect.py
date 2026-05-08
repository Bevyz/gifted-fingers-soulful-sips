import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the select element
# From: <select id="bk-service" multiple style="height: auto; min-height: 120px;">
# To: <select id="bk-service">\n          <div id="bk-service-tags" class="service-tags"></div>
select_old = '<select id="bk-service" multiple style="height: auto; min-height: 120px;">'
select_new = '<select id="bk-service">'
content = content.replace(select_old, select_new)

# Insert the tags container right after the select closing tag
idx_select = content.find('<select id="bk-service">')
if idx_select != -1:
    idx_end_select = content.find('</select>', idx_select) + 9
    tags_container = '\n          <div id="bk-service-tags" class="service-tags"></div>'
    content = content[:idx_end_select] + tags_container + content[idx_end_select:]

# 2. Add CSS
new_css = """
    .service-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 0.5rem;
    }
    .selected-tag {
      background: var(--sage-pale);
      color: var(--espresso);
      padding: 0.4rem 0.8rem;
      border-radius: 20px;
      font-size: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border: 1px solid var(--sage-light);
    }
    .tag-close {
      cursor: pointer;
      color: var(--muted);
      font-weight: bold;
      font-size: 1.1rem;
      line-height: 1;
    }
    .tag-close:hover {
      color: #ff4d4f;
    }
"""
idx_style_end = content.find('</style>')
if idx_style_end != -1:
    content = content[:idx_style_end] + new_css + content[idx_style_end:]

# 3. Add Javascript
new_js = """
  <script>
    const selectedServices = [];

    document.getElementById('bk-service').addEventListener('change', function(e) {
      const val = e.target.value;
      if (val && !selectedServices.includes(val)) {
        selectedServices.push(val);
        renderServiceTags();
      }
      e.target.value = ""; // Reset dropdown
    });

    function removeService(val) {
      const index = selectedServices.indexOf(val);
      if (index > -1) {
        selectedServices.splice(index, 1);
        renderServiceTags();
      }
    }

    function renderServiceTags() {
      const container = document.getElementById('bk-service-tags');
      container.innerHTML = '';
      selectedServices.forEach(srv => {
        const tag = document.createElement('span');
        tag.className = 'selected-tag';
        tag.innerHTML = srv + ' <span class="tag-close" onclick="removeService(\\'' + srv + '\\')">&times;</span>';
        container.appendChild(tag);
      });
    }
  </script>
"""
# Insert JS before </body>
idx_body_end = content.find('</body>')
if idx_body_end != -1:
    content = content[:idx_body_end] + new_js + content[idx_body_end:]

# 4. Update sendToWhatsApp
# Replace the lines:
# const serviceSelect = document.getElementById('bk-service');
# const selectedOptions = Array.from(serviceSelect.selectedOptions).map(opt => opt.value || opt.text);
# const service = selectedOptions.length > 0 ? selectedOptions.join(', ') : 'Not selected';
old_whatsapp_js = """const serviceSelect = document.getElementById('bk-service');
      const selectedOptions = Array.from(serviceSelect.selectedOptions).map(opt => opt.value || opt.text);
      const service = selectedOptions.length > 0 ? selectedOptions.join(', ') : 'Not selected';"""
new_whatsapp_js = "const service = selectedServices.length > 0 ? selectedServices.join(', ') : 'Not selected';"
content = content.replace(old_whatsapp_js, new_whatsapp_js)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated multiselect logic.")
