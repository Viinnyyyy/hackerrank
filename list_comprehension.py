x = list(input('Enter in x'))
y = list(input('Enter in y'))
z = list(input('Enter in z'))
n = list(input('Enter in n'))

x = list(input('Enter in x'))
y = list(input('Enter in y'))
z = list(input('Enter in z'))
n = list(input('Enter in n'))
[[x, y, z] for x in list(input('x  ')) for y in list(input('y  ')) for z in list(input('z  ')) for n in int(input('n  '))if x + y + z != n]

# begin another one


#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         [nums.index() for []]

# How can I use listcomprehension to get the best of this algorithm in line 1 marked
# list comprehension attempt

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
n = int(input("n = "))

x_list = [x for x in range(0, x+1)]
y_list = [y for y in range(0, y+1)]
z_list = [z for z in range(0, z+1)]

n = int(input("n = "))

coordinates = [[[(x, y, z) for x in range(0, x+1)] for y in range(0, y+1)] for z in range(0, z+1) if (x+y+z) != n]

coordinates_sorted = sorted([[[(x, y, z) for x in range(0, x+1)] for y in range(0, y+1)] for z in range(0, z+1) if (x+y+z) != n])
coordinates_cleaned = [[x, y, z] for x in range(0, x+1) for y in range(0, y+1) for z in range(0, z+1) if (x+y+z) != n]


coordinates_cleaned = [[[[x, y, z] for x in range(0, x+1)] for y in range(0, y+1)] for z in range(0, z+1) if (x+y+z) != n]

coordinates_stuff = [[x, y, z] for x in x_list for y in y_list for z in z_list if (x + y + z) != n]
