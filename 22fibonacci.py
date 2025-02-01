#program that reports first 10 nnumber from the fibonacci sequence
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#f(n)=f(n-1)+f(n-2)

def fibonacci():
    m=0 #f(0)=0
    n=1 #f(1)=1
    result = [m, n] #how to not use list?
    for i in range(2, 10):
        temp = i
        temp = m + n
        result.append(temp)
        m = n
        n = temp    
    return result
print(fibonacci())

def fibo():
    m=0 #f(0)=0
    n=1 #f(1)=1
    print(m)
    print(n)
    for i in range(2, 10):
        temp = i
        temp = m + n
        print(temp)
        m = n
        n = temp    

fibo()