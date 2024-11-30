if __name__ == '__main__':
    s = input()
    list_s = list(s)
    if any (word.isalnum() == True for word in list_s):
        print(True)
    else:
        print(False)
    if any (word.isalpha() == True for word in list_s):
        print(True)
    else:
        print(False)
    if any (word.isdigit() == True for word in list_s):
        print(True)
    else:
        print(False)
    if any (word.islower() == True for word in list_s):
        print(True)
    else:
        print(False)
    if any (word.isupper() == True for word in list_s):
        print(True)
    else:
        print(False)
