# Author: Srinadh chintakindi
# Code: Finding Factorial of a given number

class Fact():
    def fact(self,n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    def recursive_fact(self,n):
        if n == 0:
            return 1
        return n*self.recursive_fact(n-1)

if __name__ == "__main__":
    try:
        obj = Fact()
        value = int(input('Enter value: '))
        print(obj.fact(value))
        print(obj.recursive_fact(value))
    except Exception as e:
        print(e)