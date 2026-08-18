# Author: srinadh chintakindi
# Code: Fibonnaci series
class fib():
    def fib(self,n):
        if n == 1:
            print('0')
        elif n == 2:
            print('1')
        a,b=0,1
        for _ in range(n):
            c = a+b
            a = b
            b = c
            print(f'{c}', end=",")

try:
    obj = fib()
    limit = int(input(f'Enter a number: '))
    obj.fib(limit)
except Exception as e:
    print(f'{e}')
