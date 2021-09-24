MAX_TEMP = 102.5

temperature = float(input("Enter the substance celcius temperature: "))

while temperature > MAX_TEMP:
    print("The temperature is to high")
    print("Turn the thermostat down wait")
    print("5 minutes. Then take the temperature")
    print("again and enter it")
    temperature = float(input("Enter the new celcius temperature: "))

print("The temperature is acceptable")
print("Check it again in 15 minutes.")