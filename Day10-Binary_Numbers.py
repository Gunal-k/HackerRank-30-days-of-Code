if __name__ == '__main__':
    n = int(input().strip())
    binary_num = bin(n)[2:]
    max_one = max(map(len, binary_num.split('0')))
    print(max_one)
# Compare this snippet from Day6-Lets_Review.py: