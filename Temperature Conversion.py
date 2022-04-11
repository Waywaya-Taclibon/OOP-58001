def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class FahrenheitToCelcius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 32) * 5/9

    class KelvinToCelcius(TemperatureConversion):

        def conversion(self):
            return (self._temp - 273.15)

    class CelsiusToFahrenheit(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15

    tempInCelsius = float(input("Enter the temperature: "))

    convert = CelsiusToKelvin(tempInCelsius)

    print(str(convert.conversion()) + " From Celsius to Kelvin")

    convert = CelsiusToFahrenheit(tempInCelsius)

    print(str(convert.conversion()) + " From Celsius to Fahrenheit")

    convert = FahrenheitToCelcius(tempInCelsius)

    print(str(convert.conversion()) + " From Fahrenheit To Celsius")

    convert = KelvinToCelcius(tempInCelsius)

    print(str(convert.conversion()) + " From Kelvin To Celsius")

main()