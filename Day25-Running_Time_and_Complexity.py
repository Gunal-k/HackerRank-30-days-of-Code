import math
n1 = int(input())

for _ in range(n1):
    n = int(input())
    
    if n <= 1:
        print('Not prime')
        continue
        
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print('Prime')
    else:
        print('Not prime')