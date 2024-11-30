import sys
def minion_game(string):
    # your code goes here
    string = string.upper()
    list_string = list(string)
    vowels = ['A', 'E', 'I', 'O', 'U']

    stuart_substring = [list_string[i:] for i in [i for i, v in enumerate(list_string) if v not in vowels]]
    kelvin_substring = [list_string[i:] for i in [i for i, v in enumerate(list_string) if v in vowels]]
    
    # Counter for Stuart
    length_stuart = sum(len(substring) for substring in stuart_substring)
    # Counter for Kelvin
    length_kelvin = sum(len(substring) for substring in kelvin_substring)

    # Game decider
    if length_kelvin > length_stuart:
        print("Kelvin" , length_kelvin)
    elif length_stuart > length_kelvin:
        print("Stuart", length_stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = sys.stdin.read()
    minion_game(s)

    for line in sys.stdin:
        s.append(line)
