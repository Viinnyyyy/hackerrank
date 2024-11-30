if __name__ == '__main__':
    unsorted_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        unsorted_list.append([name, score])

    # min_names = [name for score in list if score == min(list[1])]
    # min_name = sorted(min_names)
      
    sorted_list = sorted(unsorted_list, key=lambda x: (x[1], x[0]))
    # print(sorted_list)

    sorted_name = list(zip(*sorted_list))
    # print(sorted_name)
    
    # print(*sorted_name[0], sep='\n')

    # sorted_list[0] for sorted_list[0] in sorted_list if sorted_list[1] == min(sorted_list[1])]
    for i, j in sorted_list:
        if j == sorted_list[0][1]:
            print(*i)
        # What i was trying to do was not working because i had the list wrong
        # such a draggg
        # Select the second column of the first row.
