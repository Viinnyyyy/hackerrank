def merge_the_tools(string, k):
    # your code goes here
    chunk_string = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(chunk_string)):
        print(*sorted(set(chunk_string[i]), key=chunk_string[i].index), sep='')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
