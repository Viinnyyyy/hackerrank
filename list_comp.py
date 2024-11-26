if __name__ == '__main__':
    x = int(input("x = "))
    y = int(input("y = "))
    z = int(input("z = "))
    n = int(input("n = "))

    x_list = [x for x in range(0, x+1)]
    y_list = [y for y in range(0, y+1)]
    z_list = [z for z in range(0, z+1)]

    coordinates_stuff = [[x, y, z] for x in x_list for y in y_list for z in z_list if (x + y + z) != n]
    print(coordinates_stuff)
