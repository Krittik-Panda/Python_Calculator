import os
from functions import (
    add, substraction, multiplication, division, modulus,
    check, check_positive, find_factorial, fibonacci_sequence,
    fibonacci_at_nth, sin_angle, cos_angle, tan_angle,
    compute_log, rad_to_deg, deg_to_rad
)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def calculator():
    while True:
        clear_screen()
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Check Even/Odd")
        print("7. Check Positive/Negative")
        print("8. Factorial")
        print("9. Fibonacci Sequence")
        print("10. Fibonacci nth Number")
        print("11. Sin")
        print("12. Cos")
        print("13. Tan")
        print("14. Log")
        print("15. Radian to Degree")
        print("16. Degree to Radian")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting calculator...")
            break

        clear_screen()

        if choice == 1:
            n = int(input("How many numbers? "))
            print("Result =", add(n))

        elif choice == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", substraction(a, b))

        elif choice == 3:
            n = int(input("How many numbers? "))
            print("Result =", multiplication(n))

        elif choice == 4:
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print("Result =", division(a, b))

        elif choice == 5:
            a = int(input("Enter number: "))
            b = int(input("Enter modulus base: "))
            print("Result =", modulus(a, b))

        elif choice == 6:
            n = int(input("Enter number: "))
            check(n)

        elif choice == 7:
            n = float(input("Enter number: "))
            check_positive(n)

        elif choice == 8:
            n = int(input("Enter number: "))
            print("Result =", find_factorial(n))

        elif choice == 9:
            n = int(input("Enter sequence length: "))
            print("Result =", fibonacci_sequence(n))

        elif choice == 10:
            n = int(input("Enter position n: "))
            print("Result =", fibonacci_at_nth(n))

        elif choice == 11:
            angle = float(input("Enter angle: "))
            print("sin =", sin_angle(angle))

        elif choice == 12:
            angle = float(input("Enter angle: "))
            print("cos =", cos_angle(angle))

        elif choice == 13:
            angle = float(input("Enter angle: "))
            print("tan =", tan_angle(angle))

        elif choice == 14:
            value = float(input("Enter number: "))
            print("log =", compute_log(value))

        elif choice == 15:
            rad = float(input("Enter radian: "))
            print("Degrees =", rad_to_deg(rad))

        elif choice == 16:
            deg = float(input("Enter degree: "))
            print("Radians =", deg_to_rad(deg))

        else:
            print("Invalid choice!")

        input("\nPress ENTER to continue...")

calculator()
