if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(n-1):
            if a[j] > a[j+1]:
                swaps += 1
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:    
            break
    
    print("Array is sorted in",swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])