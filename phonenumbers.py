import re
# r = "^[7-9](0-9){9}"
user_input = int(input())
validating_list = []
num_detector = re.compile(r"^[7-9](\d{9})$") 
for i in range(user_input):
    phonenumber = str(input())
    # num_detector = re.compile(r"^[7-9](\d{14})$")
    validator = num_detector.match(phonenumber)
    if validator:
        validating_list.append('YES')
    else:
        validating_list.append('NO')
print(*validating_list, sep='\n')
