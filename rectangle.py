def calc_area():
    width = float(input("\nEnter the width of the rectangle: "))
    height = float(input("\nEnter the height of the rectangle: "))
    area = width * height
    print(f"\nThe area of the rectangle is: {area:.2f}.")

def calc_perimeter():
    width = float(input("\nEnter the width of the rectangle: "))
    height = float(input("\nEnter the height of the rectangle: "))
    perimeter = 2 * (width + height)
    print(f"\nThe perimeter of the rectangle is: {perimeter:.2f}.")