# ---------------------------------------------------------------
# Temperature Converter
# Author: Roxanne Prajapati
# Description:
#      Transform user entered temperatures between Fahrenheit
#       and Celsius
# ---------------------------------------------------------------

class TemperatureConverter:

    def __init__(self):
        self.user_input = None
        self.temperature = None

    def display_prompt(self):
        """Display instructions for the user and get the user's input"""
        print("\n-------------------------------------------------------------------------------")
        print("To convert a temperature, please use one of the following formats:")
        print("1. Fahrenheit to Celsius:  Enter F followed by the temperature (e.g., F100)")
        print("2. Celsius to Fahrenheit:  Enter C followed by the temperature (e.g., C100)")
        print("-------------------------------------------------------------------------------\n")
        user_input = input("Please enter the temperature that you want to convert:")
        self.user_input = user_input


    def validate_input(self):
        """Validate the user's input format and values"""

        #Check that the input has at least 2 characters (1 letter + number)
        if len(self.user_input) < 2:
            raise ValueError("Input must start with 'F' or 'C' followed by a number.")

        # Ensure the first character is F or C
        if self.user_input[0].upper() not in ['F', 'C']:
            raise ValueError("Temperature must start with 'F' or 'C'.")

        # Check if the remaining part is a valid integer number
        try:
            int(self.user_input[1:])
        except ValueError:
            raise ValueError("Temperature value must be a whole number(integer).")


    def convert_temperature(self):
        """Check the unit(C/F) and perform the appropriate temperature conversion`"""
        unit = self.user_input[0]
        self.temperature = int(self.user_input[1:])

        if unit == "C":
            self.celsius_to_fahrenheit()
        elif unit == "F":
            self.fahrenheit_to_celsius()


    def celsius_to_fahrenheit(self):
        """Convert C to Fahrenheit"""
        result = (self.temperature * 9 / 5) + 32
        print(f"{self.user_input} is converted to {result:.2f} degrees Fahrenheit.")


    def fahrenheit_to_celsius(self):
        """Convert F to Celsius"""
        result = (self.temperature - 32) * 5 / 9
        print(f"{self.user_input} is converted to {result:.2f} degrees Celsius.")



# Run the program only when executed directly
if __name__ == "__main__":
    temperature = TemperatureConverter()

    # Loop until the user chooses to stop
    while True:
        try:
            temperature.display_prompt()
            temperature.validate_input()
            temperature.convert_temperature()

            # Ask user if they want another conversion, if no exit the loop
            again = input("Do you want to convert another temperature? (Y/N): ").strip().upper()

            if again != "Y":
                print("\nThank you for using this Temperature Converter.!")
                break

        except ValueError as e:
            """Handle invalid input and restart loop"""
            print("Invalid input:", e)
            print("Please try again.\n")

