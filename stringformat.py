def print_formatted(number):
    # your code goes here
    # for num in range(int(number)+1):
    #     decimal = num+1
    #     octadecimal = oct(demical)[2:]
    #     hexadecimal = hex(decimal)[2:]
    #     binary = bin(decimal)[2:]
    #     print(decimal, octadecimal, hexadecimal, binary, sep='')
    bin_width = len(bin(number)[2:]) 
    for x in range(1, number+1):
        print(repr(x).rjust(bin_width), end=' ')
        print(oct(x)[2:].rjust(bin_width), end=' ')
        print(('%X' % x).rjust(bin_width), end=' ')
        print(bin(x)[2:].rjust(bin_width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
