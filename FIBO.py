#반복문을 이용한 피보나치 수열
def interfibo(n) :
    one = 0
    two = 1

    if n == 0 :
        return 0

    elif n == 1 :
        return 1

    else :
        for i in range(n-1) :
            fibo = one + two
            one = two
            two = fibo

        return fibo

#재귀함수를 이용한 피보나치 수열
def fibo(n) :
    if n <= 1 :
        return n
    return fibo(n-1) + fibo(n-2)

#main 함수
import time

while 1 :
    num = int(input('Write number you want : '))

    if num == -1 :
        break

    t1 = float(time.time())
    myfibo = fibo(num)
    mytime = float(time.time())-t1
    print("Fibo(%d) = %d\ntime = %.6f\n" %(num, myfibo, mytime))

    t1 = float(time.time())
    myfibo = interfibo(num)
    mytime = float(time.time()) - t1
    print("Interfibo(%d) = %d\ntime = %.6f\n" %(num, myfibo, mytime))