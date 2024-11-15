#zad1
liczba = int(input("Podaj liczbę: "))

if liczba < 0:
    print("Błąd:")
else:
    a1 = liczba
    a2 = 1  

    for _ in range(10):
        a2 = (a1 + liczba / a1) / 2
        a1 = a2

    print(f"Pierwiastek kwadratowy z {liczba} = {a2}")