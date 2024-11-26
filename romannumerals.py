import re
regex_pattern = re.compile(r"""^M{0,3}
                    (CM|CD|D?C{0,3})?
                    (XC|XL|L?X{0,3})?
                    (IX|IV|V?I{0,3})?$""", re.VERBOSE)# Do not delete 'r'.


import re
print(str(bool(re.match(regex_pattern, input()))))
