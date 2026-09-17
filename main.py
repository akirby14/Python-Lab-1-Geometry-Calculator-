import circle
import rectangle

def calculator_prompt():
    num_choices = ["1", "2", "3", "4", "5"]
    choice = " "
    
    while choice != 5:
        print("\nGeometry Calculator \n-------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice not in num_choices:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

        else:
            choice = int(choice)
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