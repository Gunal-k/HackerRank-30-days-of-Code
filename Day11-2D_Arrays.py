if __name__ == '__main__':

    arr = []
    maxsum = float('-inf')
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            currsum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            
            maxsum = max(maxsum,currsum)
            
    print(maxsum)