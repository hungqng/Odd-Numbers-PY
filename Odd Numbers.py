def oddNumbers(l, r):
    # Write your code here
    arr = []
    
    for num in range(l, r+1):
        if num % 2 != 0:
            arr.append(num)
    return arr