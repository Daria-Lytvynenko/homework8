if __name__ == '__main__':
    #Task 2. Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then
    #returns the  value of squared a divided by b, construct a try-except block which raises an exception if
    #the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
    a = int(input("Please input first number:"))
    b = int(input("Please input second number:"))
    x=int()
    def dividing(a, b):
        x=a**2/b
        try:
            a**2/b
        except ZeroDivisionError:
            print("not divided by 0")
        except ValueError:
            while False:
                a.isdigit() and b.isdigit()
                print('Only numbers can be input')
        print (x)
    dividing(a,b)