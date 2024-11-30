def mutate_string(string, position, character):
    string = s[:int(i)] + str(c) + s[int(i):]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
