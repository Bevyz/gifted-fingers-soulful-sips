import re

file_path = r'c:\Users\ikuda\Downloads\gifted-fingers-soulful-sips\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="booking"')
if idx != -1:
    # Just look for the <form> inside the booking section
    idx_form = content.find('<form', idx)
    if idx_form != -1:
        idx_end_form = content.find('</form>', idx_form) + 7
        form_content = content[idx_form:idx_end_form]
        print(form_content)
    else:
        print("No form found")

