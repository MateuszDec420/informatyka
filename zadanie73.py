with open("tekst.txt") as plik:
    tekst = plik.readline()
print(tekst)
lista_napisow = tekst.split()
print(lista_napisow)
licznik = 0 
for napis in lista_napisow:
    for i in range(len(napis)-1):
        if napis[i] == napis[i+1]:
            licznik += 1
            break
print(licznik)
slownik ={}
for znak in tekst:
    if znak !=" " and znak !="\n":
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
print(sorted(slownik.items()))
suma = sum(slownik.values())
for krotka in sorted(slownik.items()):
    print(krotka[0],'':',krotka[1],"(),round(100*krotka[1]/suma,2),'%')")

samogloski = 'AEIOUY'
maks = 0
for napis in lista_napisow:
    n = 0
    for litera in napis:
        if litera not in samogloski:
            n += 1
    if n > maks:
        maks = n
    else:
print(maks)