if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    largest = max(arr)

    arr_good = [i for i in arr if i != largest]
    secondLargest = max(arr_good)
    print(secondLargest)
