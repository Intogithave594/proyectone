# ============================================================
# CALCULADORA / CALCULATOR
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero / Cannot divide by zero")
    return a / b

def get_number(prompt):
    while True:
        try:
            text = input(prompt)
            return float(text)
        except ValueError:
            print("Error: escribe un número válido / Please enter a valid number.")

def main():
    operations = {
        "1": ("Sumar/Add", add),
        "2": ("Restar/Subtract", subtract),
        "3": ("Multiplicar/Multiply", multiply),
        "4": ("Dividir/Divide", divide),
    }

    print("=== CALCULADORA / CALCULATOR ===")

    while True:
        print("\nOperaciones / Operations:")
        print("  1. Sumar / Add        (+)")
        print("  2. Restar / Subtract  (-)")
        print("  3. Multiplicar / Multiply (*)")
        print("  4. Dividir / Divide   (/)")
        print("  5. Salir / Quit       (q)")

        choice = input("Elige una opción / Choose an option: ").strip()

        if choice in ("5", "q", "Q", "salir", "quit"):
            print("¡Adiós! / Goodbye!")
            break

        if choice not in operations:
            print("Opción no válida / Invalid option.")
            continue

        name, operation = operations[choice]
        a = get_number("Primer número / First number:  ")
        b = get_number("Segundo número / Second number: ")

        try:
            result = operation(a, b)
            print(f"Resultado / Result: {a} y/and {b} -> {result}")
        except ZeroDivisionError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()