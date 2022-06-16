""""Bimestral"""

# Entradas
print("-----------------------")
print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir):")
print("-----------------------")
retiro = float(input())

# Inicio ciclo mientras

while retiro > 0:
    # Calculos
    monedas_de_100 = retiro
    billetes_de_10000 = (monedas_de_100-monedas_de_100%10000)/10000
    monedas_de_100 = monedas_de_100%10000
    billetes_de_2000 = (monedas_de_100-monedas_de_100%2000)/2000
    monedas_de_100 = monedas_de_100%2000/100
    # Salidas
    print("Cantidad billetes de 10000: ",billetes_de_10000)
    print("Cantidad billetes de 2000: ",billetes_de_2000)
    print("Cantidad monedas de 100: ",monedas_de_100)
    # Reinicio
    print("Ingresa el valor a retirar en multiplos de 100 (Cero para salir): ")
    retiro = float(input())
print("Programa terminado")