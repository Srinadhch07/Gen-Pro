# Author: sriandh chintakindi
# Code: palindrome or not

class Palindrome():
    def __init__(self, number):
        if str(number) == str(number)[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")
    def is_palindrome(self, number):
        self.number = number
        sum = 0
        while number > 0:
            digit = number % 10
            number = number //10
            sum = sum * 10 + digit
        print("Palindrome") if self.number == sum else print("Not Palindrome")

if __name__ == "__main__":
    try:
        number = int(input("Enter number: "))
        obj = Palindrome(number)
        obj.is_palindrome(number)
    except Exception as e:
        print(e)
