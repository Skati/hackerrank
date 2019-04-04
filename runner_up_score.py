if __name__ == '__main__':
    n = 5
    arr = [2,3,1,6,6]
    m=max(arr)
    for i in range(0,n):
        if max(arr)==m:
            arr.remove(max(arr))
    arr.sort(reverse=True)
    print(arr[0])
