# Author: Srinadh chintakindi
# Code: Armstrong number using only logics

class ArmStrong():
    def armstrong(self, number):
        original = number
        count = len(str(number))
        sum = 0
        while number > 0:
            digit = number % 10
            number = number // 10
            sum += digit ** count
        print("is ArmStrong number: True") if original == sum else print("is ArmStrong number: False")


if __name__ == "__main__":
    value = int(input("Enter value: "))
    obj  = ArmStrong()
    obj.armstrong(value)

