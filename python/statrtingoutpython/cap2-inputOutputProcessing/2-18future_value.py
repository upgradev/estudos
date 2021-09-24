future_value =  float(input("enter the desired future value "))

rate = float(input("enter the annual interest rate: "))

years = int(input("enter yhe number of years the money will grow: "))

present_value = future_value / (1.0 + rate) ** years

print('you will need to deposit this amount: ',present_value)