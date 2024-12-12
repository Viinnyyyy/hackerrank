import re
user_input = int(input())
validating_list = ''
hex_detector = r".#[a-fA-F0-9]{6}|.#[a-fA-F0-9]{3}"
for i in range(user_input):
    code_line = str(input())
    print(code_line)
    validator = re.findall(hex_detector, code_line)
    # print(validator)
    validating_list = validating_list + ('\n'.join(validator))
# print('\n'.join(validating_list))
print(validating_list, sep='\n')

