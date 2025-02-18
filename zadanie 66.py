
def suma_cyfr(Liczba): #liczba jest jako string
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

def pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba == 2:
        return True 
    if liczba % 2 == 0:
        return False
    for i in range(3,int(liczba**0.5)+1,2):
        if liczba % i == 0:
            return False
    return True

lista_trojek = []
with open("trojki.txt") as plik:
    for linia in plik:
        lista_trojek.append(linia.split())
print(lista_trojek)

for liczby in lista_trojek:
    if suma_cyfr(liczby[0]) + suma_cyfr(liczby[1]) == suma_cyfr(liczby[2]):
        print(liczby)

for liczby in lista_trojek:
    if int(liczby[0]) + int(liczby[1]) == int(liczby[2]):
        if pierwsza(int(liczby[0])) and pierwsza(int(liczby[1])):
            print(liczby)
