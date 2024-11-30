def swap_case(s):
    string = ''
    for i in range(len(s.rstrip())):
        string += ''.join(s[i].swapcase()) 
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
