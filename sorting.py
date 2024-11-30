if __name__ == "__main__":
    astring = list(str(input())) 
    print(*astring)
    print(astring)
    print(*astring, sep="")

    # astring_sorted = sorted(astring)
    # def sorting_algorithm(unsorted_astring):
    #     for char in unsorted_astring:
    #         if type(char) == astring:
    #             do something
    #         elif type(char) == int and char % 2 == 0:
    #             do something
    #         elif type(char) == int and char % 2 == 0:
    #             do something

    # sorted_list = sorted(astring, key=lambda x)
    upper = []
    lower = []
    odd = []
    even = []
    number = []
    for char in astring:
        if char.islower():
            lower+=char
        if char.isupper():
            upper+=char
        elif char.isnumeric():
            if int(char) % 2 == 0:
                even+=char
            else:
                odd+=char
    sorted_lower = sorted(lower)
    sorted_upper = sorted(upper)
    sorted_odd = sorted(odd)
    sorted_even = sorted(even)
    print(*sorted_lower, sep='')
    print(*sorted_upper, sep='')
    print(*sorted_odd, sep='')
    print(*sorted_even, sep='')
    sorted_astring = sorted_lower + sorted_upper + sorted_odd + sorted_even
    print(*sorted_astring, sep='')
    # sep_alpha = sorted(alpha, key=str.istitle)
    # sorted_alpha = sorted(sep_alpha, key=str.isalpha)
    # sorted_trial = sorted(astring, key=str.isalpha)
    # sorted_trial2 = sorted(astring, key=str.isdigit)
    # sorted_trial3 = sorted(astring, key=str.title)
    # sorted_trial3b = sorted(alpha, key=str.title)
    # sorted_trial4 = sorted(astring, key=str.islower)
    # sorted_trial4b = sorted(alpha, key=str.islower)
    # sorted_trial4c = sorted(alpha, key=str.ascii_lowercase)
    # print(*sep_alpha, sep="")
    # print(*sorted_alpha, sep="")
    # print(*number, sep="")
    # print(*sorted_trial)
    # print(*sorted_trial2)
    # print(*sorted_trial3)
    # print(*sorted_trial3b)
    # print(*sorted_trial4)
    # print(*sorted_trial4b)
    # print(*sorted_trial4c, sep='')
