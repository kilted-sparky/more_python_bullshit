# Odd or even Exercise
# code to check if the number entered is odd or even

num = int(input("Enter a number: "))
while True:
    if num % 2 == 0:
        num = "Even"
        print("Even")
    else:
        num = "Odd"
        print("Odd")
        break