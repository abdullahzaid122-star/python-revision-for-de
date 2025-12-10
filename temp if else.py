temperature = float(input("enter the temp: "))
unit = input("is it in celsius or fahrenheit? (c/f): ")
if unit=="c":
    fahrenheit = (temperature * 9/5) + 32
    print(fahrenheit, "is the temperature in fahrenheit")
elif unit=="f":
     celsius = (temperature-32) * 5/9
     print(celsius, "is the temperature in celsius is")