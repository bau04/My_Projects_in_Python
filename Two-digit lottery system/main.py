import random

print("Welcome to the 2-digit lottery draw")
print("Choose a number from 0-9")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

x1 = int(random.randint(0,9))
x2 = int(random.randint(0,9))

if n1 == x1 and n2 == x2:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2)
    print("Your pick: " , n1 , " , " , n2)
    print("Result: You Won!!!")

elif n1 <= -1 or n2 <= -1 :
    print("Error: The number you picked is below the range")

elif n1 >= 10 or n2 >= 10 :
    print("Error: The number you picked is above the range ")

elif n1 != x1 or n2 != x2:
    print("\nToday's lottery result is: ")
    print("Winning number: " , x1 , " , " , x2)
    print("Your pick: " , n1 , " , " , n2)
    print("Result: You lost")
