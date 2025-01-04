import re
user_input = int(input())
css_string = ""
for i in range(user_input):
    css_string += input()
section_detector = r"{.*?}"
hex_detector = r"#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3}"

sections = re.findall(section_detector, css_string)
for section in sections:
    print(*re.findall(hex_detector, section), sep='\n')
