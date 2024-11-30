if __name__ == '__main__':
    unsorted_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        unsorted_list.append([name, score])

    sorted_list = sorted(unsorted_list, key=lambda x: (x[1], x[0]))

    sorted_second_list = [[i, j] for i, j in sorted_list if j != sorted_list[0][1]]

    sorted_name = list(zip(*sorted_list))
    for i, j in sorted_second_list:
        if j == sorted_second_list[0][1]:
            print(i)
