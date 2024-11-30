def count_substring(string, sub_string):
    j=0
    searched_string = []
    while len(sub_string)+j in range(0, len(string)+1):
        searched_string.append(string[j:len(sub_string)+j])
        j += 1
    i = 0
    for word in searched_string:
        if word == sub_string:
            i += 1
    return i

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
