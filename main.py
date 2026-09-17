import circle
import rectangle

'''
Aliases are necessary when importing these modules to prevent naming conflicts with the functions in the file.
'''

def calculator_prompt():
    num_choices = ["1", "2", "3", "4", "5"]
    choice = " "
    answer = 0

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
                print(f"\nThe area of the circle is: {circle.calc_area(answer):.2f}.")
                input("\nPlease press Enter to continue...")
            elif choice == 2:
                print(f"\nThe circumference of the circle is: {circle.calc_area(answer):.2f}.")
                input("\nPlease press Enter to continue...")

            elif choice == 3:
                print(f"\nThe area of the rectangle is: {rectangle.calc_area(answer):.2f}.")
                input("\nPlease press Enter to continue...")

            elif choice == 4:
                print(f"\nThe perimeter of the rectangle is: {rectangle.calc_perimeter(answer):.2f}.")
                input("\nPlease press Enter to continue...")

            elif choice == 5:
                print("\nGoodbye!")

calculator_prompt()