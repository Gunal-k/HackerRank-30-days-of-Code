def bitwiseAnd(N, K):
    max_val = 0
    for i in range(N-1,0,-1):
        for j in range(N,i,-1):
            val = i&j
            if val < K:
                max_val = max(val,max_val)
                if max_val == K-1:
                    return max_val
    
    return max_val
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        res = bitwiseAnd(count, lim)
        fptr.write(str(res) + '\n')

    fptr.close()