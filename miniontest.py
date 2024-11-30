def minion_game(string):
    # your code goes here
    string = string.upper()
    list_string = list(string)
    vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart_index = [i for i, v in enumerate(list_string) if v not in vowels]
    print(Stuart_index)
    Kelvin_index = [i for i, v in enumerate(list_string) if v in vowels]
    print(Kelvin_index)

    # Counter for Stuart
    Stuart_count = 0
    for i in Stuart_index:
        sub_string = list_string[i:]
        for k, v in enumerate(sub_string):
            print(sub_string[0:k+1])
            Stuart_count += 1
    print(Stuart_count)

    # Counter for Kelvin
    Kelvin_count = 0
    for i in Kelvin_index:
        sub_string = list_string[i:]
        for k, v in enumerate(sub_string):
            print(sub_string[0:k+1])
            Kelvin_count += 1
    print(Kelvin_count)

    # Game decider
    if Kelvin_count > Stuart_count:
        print("Kelvin " , Kelvin_count)
    elif Stuart_count > Kelvin_count:
        print("Stuart ", Stuart_count)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
