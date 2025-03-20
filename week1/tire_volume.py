#Problem Statement
#The size of a car tire in the United States is
#  represented with three numbers like this: 205/60R15. 
# The first number is the width of the tire in millimeters.
#  The second number is the aspect ratio.
#  The third number is the diameter
#  in inches of the wheel that the tire fits. 
# The volume of space inside a tire can be approximated with this formula:

#varialbes
#v is the volume in liters,
#π is the constant PI, which is the ratio of the circumference 
# of a circle divided by its diameter (use math.pi),
#w is the width of the tire in millimeters,
#a is the aspect ratio of the tire, and
#d is the diameter of the wheel in inches.
from datetime import datetime
import math
#inputs
# Función para eliminar el .0 si el número es entero
def remove_decimal(value):
    if value.is_integer():
        return int(value)
    return value



def get_tire_price(w, a, d):
    # Condiciones hipotéticas de precios
    if w == 185 and a == 60 and d == 15:
        return 100
    elif w == 205 and a == 55 and d == 16:
        return 120
    elif w == 225 and a == 50 and d == 17:
        return 140
    elif w == 215 and a == 60 and d == 16:
        return 110
    else:
        return 150  # Precio por defecto para otros tamaños

w=float(input("please Enter the width of the tire in mm:"))
a=float(input("please Enter the aspect ratio of the tire:"))
d=float(input("please Enter the diameter of the wheel in inches:"))

w = remove_decimal(w)
a = remove_decimal(a)
d = remove_decimal(d)

#formula

v = round((math.pi * w**2 * a * (w * a + 2540 * d)) / 10_000_000_000,2)

print("The volume of space inside a tire is approximate",v,"liters")
price = get_tire_price(w, a, d)
print(f"The price of the tire is: ${price}")
buy_tire = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
current_date = datetime.now().date()

#......Exceeding the Requirements.........

if buy_tire == "yes":
    # Ask for the user's phone number
    phone_number = input("Please enter your phone number: ")

    # Open the file for appending
    with open('volumes.txt', mode="a") as file2:
        # Write the data in the correct format (date width aspect ratio diameter volume price phone number)
        file2.write(f"{current_date}, {w}, {a}, {d}, {v}, ${price}, {phone_number}\n")

    print("Your information has been saved in volumes.txt.")

else:
    # If the user doesn't want to buy, still append the data without the phone number
    with open('volumes.txt', mode="a") as file2:
        # Write the data in the correct format (date width aspect ratio diameter volume price)
        file2.write(f"{current_date}, {w}, {a}, {d}, {v}, ${price}\n")

    print("The data has been saved in volumes.txt.")
#print(v,file=file2)160
#print(f"{current_date}, {w}, {a}, {d}, {v}", sep=" ", end="\n", file=file2, flush=False)