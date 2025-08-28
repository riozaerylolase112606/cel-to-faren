
def convert_temperature(celsius):
    fahrenheit = (9/5) * celsius + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Input from user
c = float(input("Enter temperature in Celsius: "))
f, k = convert_temperature(c)

print(f"Fahrenheit: {f:.2f}")
print(f"Kelvin: {k:.2f}")
