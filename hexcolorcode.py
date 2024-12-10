import re
code_lines = []
while True:
    code_line = input()
    if code_line:
        code_lines.append(code_line)
    else:
        break
# line_string = user_string.split('\n')
code_length = int(code_lines[0])
validating_list = []
hex_detector = r"#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6}"
for line in code_lines[1:]:
    validator = re.findall(hex_detector, line)
    validating_list.append(*validator)
# print('\n'.join(validating_list))
print(*validating_list, sep='\n')

