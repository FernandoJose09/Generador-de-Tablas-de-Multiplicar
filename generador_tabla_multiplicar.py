def generar_tabla_multiplicar(numero):
    for i in range(1, 13):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        numero = int(input("Ingresa un número para ver su tabla de multiplicar (hasta el 12): "))
        print(f"\nTabla de multiplicar del {numero}:")
        generar_tabla_multiplicar(numero)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
