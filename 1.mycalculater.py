# Pehle hum user se do numbers lenge
num1 = float(input("Pehla number daalo: "))
num2 = float(input("Dusra number daalo: "))

# Ab user se operation poochenge (+, -, *, /)
operator = input("Kaunsa operation karna hai? (+, -, *, /) : ")

# Ab 'if-elif-else' ka istemal karke calculation karenge
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Yahan check karenge ki kahin dusra number zero to nahi
    if num2 == 0:
        result = "Error! Zero se divide nahi kar sakte."
    else:
        result = num1 / num2
else:
    result = "Galat operator daala hai!"

# Aakhir me result print kar denge
print("--------------------")
print(f"Result hai: {result}")
print("--------------------")