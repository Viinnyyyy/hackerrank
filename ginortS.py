if __name__ == "__main__":
    astring = list(str(input())) 
    
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
    sorted_astring = sorted_lower + sorted_upper + sorted_odd + sorted_even
    print(*sorted_astring, sep='')
