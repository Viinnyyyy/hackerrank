def print_rangoli(size):
    # your code goes here
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = alphabets[0:size]
    pattern = []
    for i in range(0, size):
        list_pattern = list(reversed(alphabet)) + alphabet[1:]
        string_pattern = '-'.join(list_pattern)
        pattern.append(string_pattern.center(((size*4) - 3), '-'))
        alphabet.pop(0)
    print(*(reversed(pattern)), sep='\n')
    print(*pattern[1:], sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
