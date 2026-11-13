a = float(input("Primer número / First number: "))
b = float(input("Segundo número / Second number: "))

op = input("¿Operación? (+ - * /): ").strip()

if op == "+":
    print("Resultado / Result:", a + b)
elif op == "-":
    print("Resultado / Result:", a - b)
elif op == "*":
    print("Resultado / Result:", a * b)
elif op == "/":
    print("Resultado / Result:", a / b)
else:
    print("Opción no válida / Invalid option")