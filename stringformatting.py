def print_formatted(number):
    bin_width = len(bin(number)[2:]) 
    for x in range(1, number+1):
        print(repr(x).rjust(bin_width), end=' ')
        print(oct(x)[2:].rjust(bin_width), end=' ')
        print(('%X' % x).rjust(bin_width), end=' ')
        print(bin(x)[2:].rjust(bin_width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
