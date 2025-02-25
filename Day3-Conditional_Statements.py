if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 == 0:
        if N == 2:
            print("Not Weird")    
        elif N in range(6,20+1):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")