class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + self.num2
    def __sub__(self, other):
        return self.num1 - self.num2
    def __mul__(self, other):
        return self.num1 * self.num2
while True:

    c1 = input(f"Enter Type of Calculation you want {1}.addistion {2}.subtract {3}.multiply {4}.Quit: ")
    if c1 =="4":
        quit()
    else:
        None
    c2 = int(input("Enter first Number: "))
    c3 = int(input("Enter second Number: "))



    cal1 = Calculator(c2, c3)
    cal2 = Calculator(c2, c3)



    addistion = (cal1 + cal2)
    subtract = (cal1 - cal2)
    multiply = (cal1 * cal2)



    if c1 == "1":
        print(c2 + c3)
    elif c1 == "2":
        print(c2 - c3)
    elif c1 == "3":
        print(c2 * c3)
    else:
        print('sorry you did not type the right number please try again')



