# Convierte un precio en pesos a dólares
"""
1. Pedir el valor del dolar (dolar)
2. Pedir el precio del producto en pesos (precioPesos)
3. precioDolares = precioPesos/dolar
4. Escribir (precioDolares)"""

dolar = float(input("Introduce el tipo de cambio del dólar: "))
precioPesos = float(input("Introduce el precio del producto: "))
precioDolares = precioPesos/dolar
print("EL precio del producto en dolares es: ", precioDolares)          
            