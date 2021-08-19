#求最大公约数 欧几里得辗转相除法 
#1. 当最小值为最大公约数时，直接返回；
#2. 当最小值不为最大公约数时，最大公约数不会大于最小值的1/2；
#3. 求最大公约数理应从大到小循环递减求最大。
def gcd(a,b):
    if b>a:
        a,b=b,a
    if a%b==0:
        return b
    for i in range(b//2+1,1,-1):
        if b%i==0 and a%i==0:
            return i

while 1:
    a=int(input('a:'))
    b=int(input('b:'))
    print(gcd(a,b))
