def show_menu():
    print("Welcome to the temperature converter application🌡️")
    print("1. Celsius --> Fahrenheit")
    print("2. Fahrenheit --> Celsius")
    print("3. Celsius --> Kelvin")
    print("4. Fahrenheit --> Kelvin")
    print("5. Kelvin --> Fahrenheit")
    print("6. Kelvin --> Celsius")
    print("7. Exit")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Choose the number between 1 - 7 from the menu: "))
        
            if choice == 7:
                print("Existing.")
                break
        
            if choice > 7 or choice < 1:
                print("Only numbers between 1 - 7 is valid input. Try again")
                continue

            temperature = float(input("Enter the temperature \n(negative values are also allowed for fahrenheit & celcius only):"))

            if choice in [5, 6] and temperature < 0:
                print("❌ Kelvin temperature cannot be negative.")
                continue

            if choice == 1:
                result = celsius_to_fahrenheit(temperature)

            elif choice == 2:
                result = fahrenheit_to_celsius(temperature)

            elif choice == 3:
                result = celsius_to_kelvin(temperature)

            elif choice == 4:
                result = fahrenheit_to_kelvin(temperature)

            elif choice == 5:
                result = kelvin_to_fahrenheit(temperature)

            elif choice == 6:
                result = kelvin_to_celsius(temperature)

            print(f"Result: {result:.2f}")

        except ValueError:
            print("❌ Invalid input only numbers are allowed.")

main()