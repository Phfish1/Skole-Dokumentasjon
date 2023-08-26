def fahrenheit_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

temperatur = float(input("Skriv temperatur (F): "))
temperatur_celcius = fahrenheit_to_celsius(temperatur)

print(temperatur_celcius)

