def raise_power():
    power_result = base ** power
    return power_result


base = int(input('Enter the base number: '))
power = int(input('Enter the power number: '))
final_result = raise_power()
print(f"Answer is {final_result}")