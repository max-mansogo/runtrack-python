
def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Operator non valide"

print(calcule(5, '+', 3))  
print(calcule(10, '-', 4))  
print(calcule(2, '*', 6))  
print(calcule(10, '/', 2))  
print(calcule(7, '%', 3))  
print(calcule(5, '^', 3))  # Output: Operator non valide

