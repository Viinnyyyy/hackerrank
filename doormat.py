if __name__ == '__main__':
    n, m = int(input()), int(input())
    pattern = '.|.'
    ws = '-'
    welcome = "WELCOME"
    pattern_list = []
    # for i in range(n):
    #     top = top.center(int(m), '.|.')
    # for i in range(int((n-1)/2)):
    #     print((pattern*(1+(2*i))).center(m, ws))
    # print(welcome)
    # for i in range(n-1, n, -i):
    #     print((pattern*(1+(2*i))).center(m, ws))

    for i in range(int((n-1)/2)):
        pattern_list.append((pattern*(1+(2*i))).center(m, ws))
    print(*pattern_list, sep='\n')
    print(welcome.center(m, ws))
    print(*(sorted(pattern_list, reverse=True)), sep='\n')

