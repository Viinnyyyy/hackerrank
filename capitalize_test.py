import re

def solve(s):
    s_list = re.split(r'(\W+)', s)
    new_s = []
    for name in s_list:
        new_name = name.replace(name[0], name[0].upper(), 1)
        new_s.append(new_name)
    new_s_string = ''.join(new_s)
    print(new_s_string)

s = input()
solve(s)
