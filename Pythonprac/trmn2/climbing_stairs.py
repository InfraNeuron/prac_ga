n=5

def calculate_res(n):
    if n <= 2:
        return n
    else:
        a,b=1,2
        for _ in range(3,n+1):
            a,b=b,a+b
        return b

print("The result is",calculate_res(n))

