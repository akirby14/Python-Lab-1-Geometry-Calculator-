import circle
import rectangle

def calculator_prompt():
    choice = 0
    while choice != 5:
        print("Geometry Calculator \n-------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")

        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 1:
            circle.calc_area()
            input("\nPlease press Enter to continue...")
        elif choice == 2:
            circle.calc_circumference()
            input("\nPlease press Enter to continue...")
        elif choice == 3:
            rectangle.calc_area()
            input("\nPlease press Enter to continue...")
        elif choice == 4:
            rectangle.calc_perimeter()
            input("Please press Enter to continue...")
        elif choice == 5:
            print("\nGoodbye!")

calculator_prompt()