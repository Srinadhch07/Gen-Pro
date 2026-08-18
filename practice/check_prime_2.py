# Author: Srinadh chintakindi
# Code: Checking prime or not using millar-robin primality test

class is_prime():
    def prime(self, n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
            
        return True
if  __name__ == "__main__":
    try:
        value = int(input('Enter value: '))
        obj = (is_prime())
        print(obj.prime(value))
    except Exception as e:
        print(f'program failed: {e}')
