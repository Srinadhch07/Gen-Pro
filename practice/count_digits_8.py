# Author: Srinadh chintakindi
# Code: Count number of digits in a number 

class CountDigits():
    def __init__(self, number):
        self.number = number
        count = 0
        while number > 0:
            count += 1
            number = number //10
        print(f'Number of digits: {count}')
    def count_digits(self, number):
        print(f'Number of Digits: {len(str(number))}')


if __name__ == "__main__":
    try:
        number = int(input("Enter Number: "))
        obj = CountDigits(number)
        obj.count_digits(number)

    except Exception as e:
        print(e)