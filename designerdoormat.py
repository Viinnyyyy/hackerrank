if __name__ == '__main__':
    n, m = map(int, input().split())
    pattern = '.|.'
    ws = '-'
    welcome = "WELCOME"
    pattern_list = []

    for i in range(int((n-1)/2)):
        pattern_list.append((pattern*(1+(2*i))).center(m, ws))
    print(*pattern_list, sep='\n')
    print(welcome.center(m, ws))
    print(*(sorted(pattern_list, reverse=True)), sep='\n')

