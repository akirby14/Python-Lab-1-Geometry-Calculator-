
def calc_area():
    radius = float(input("\nEnter the radius of the circle: "))
    area = 3.14159 * (radius ** 2)
    print(f"\nThe area of the circle is: {area:.2f}.")

def calc_circumference():
    radius = float(input("\nEnter the radius of the circle: "))
    circumference = 2 * 3.14159 * radius
    print(f"\nThe circumference of the circle is: {circumference:.2f}.")
