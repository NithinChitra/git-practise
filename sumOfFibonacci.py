def sumOfFibonacciSeries(n):
    if n<=0:
        return
    if n==1:
        return 0
    if n==2:
        return 1
    a=0
    b=1
    count=3
    sum=1
    while count<=n:
        c=a+b
        sum+=c
        a=b
        b=c
        count+=1
    return sum
print(sumOfFibonacciSeries(5))
