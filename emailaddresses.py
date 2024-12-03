import re
user_input = int(input())
validating_list = []
email_detector = re.compile(r"""^<[a-zA-Z][a-zA-Z0-9._-]+
                            @[a-zA-Z]+
                            \.[a-zA-Z]{1,3}>$
                            """, re.VERBOSE) #<----change to the valid email.We might have to use verbose on it for readability
for i in range(user_input):
    name_emailaddress = str(input())
    emailaddress = str(name_emailaddress.split(" ")[1])
    # valid = re.match(email_detector, emailaddress)
    validator = email_detector.match(emailaddress)
    if validator:
        validating_list.append(name_emailaddress)
    else:
        None
print(*validating_list, sep='\n')
