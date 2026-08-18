# Author: Srinadh chintakindi
# Code: Reverse number using only logics

class ReverseNumber():
    def __init__(self, number):
        self.number = number
        reverse_number = 0
        while number > 0:
            digit = number % 10
            number = number // 10
            reverse_number = reverse_number * 10 + digit
        print("Reverse number: ", reverse_number)

if __name__ == "__main__":
    try:
        number = int(input("Enter number: "))
        ReverseNumber(number)
    except Exception as e:
        print(e)