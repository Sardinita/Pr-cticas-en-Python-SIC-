import random 
while True:
    coin = int (input("Cara (1) o sello (0)?\n>>>  "))
    res = random.randrange(0,2)
    if coin == res:
        if res == 1:
            print(("Ganaste, la moneda es Cara"))
        else:
            print("Ganaste la moneda es Sello")
    else:
        print(f"Perdiste, el resultado es {res}")
    continuar = str(input("Desea continuar?s/n\n>>>  "))
    if continuar.lower() != 's':
        break