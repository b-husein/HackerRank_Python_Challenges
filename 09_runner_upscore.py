if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    i = 0

    while i < n and arr[i+1] == arr[i]:
        i = i+1

    print(arr[i + 1])
