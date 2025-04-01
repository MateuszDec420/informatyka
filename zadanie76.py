
def szyfruj_napis(napis, klucz):
    n = len(klucz)
    napis = list(napis)
    for i in range(len(napis)):
        j = klucz[(i % n)] - 1
        napis[i], napis[j] = napis[j], napis[i]
    return ''.join(napis)


def zadanie_76_1():
    with open('szyfr1.txt', 'r') as plik:
        linie = plik.readlines()
        napisy = [linia.strip() for linia in linie[:6]]
        klucz = list(map(int, linie[6].strip().split()))
    
    zaszyfrowane_napisy = [szyfruj_napis(napis, klucz) for napis in napisy]
    
    with open('wyniki_szyfr1.txt', 'w') as plik_wynikowy:
        for zaszyfrowany in zaszyfrowane_napisy:
            plik_wynikowy.write(zaszyfrowany + '\n')

def zadanie_76_2():
    with open('szyfr2.txt', 'r') as plik:
        linie = plik.readlines()
        napis = linie[0].strip()
        klucz = list(map(int, linie[1].strip().split()))
    
    zaszyfrowany_napis = szyfruj_napis(napis, klucz)
    
    with open('wyniki_szyfr2.txt', 'w') as plik_wynikowy:
        plik_wynikowy.write(zaszyfrowany_napis + '\n')

def odszyfruj_napis(napis, klucz):
    n = len(klucz)
    odwrotny_klucz = [0] * n
    for i, k in enumerate(klucz):
        odwrotny_klucz[k - 1] = i + 1
    
    napis = list(napis)
    for i in range(len(napis) - 1, -1, -1):
        j = odwrotny_klucz[(i % n)] - 1
        napis[i], napis[j] = napis[j], napis[i]
    return ''.join(napis)

def zadanie_76_3():
    with open('szyfr3.txt', 'r') as plik:
        napis = plik.readline().strip()
    
    klucz = [6, 2, 4, 1, 5, 3]
    odszyfrowany_napis = odszyfruj_napis(napis, klucz)
    
    with open('wyniki_szyfr3.txt', 'w') as plik_wynikowy:
        plik_wynikowy.write(odszyfrowany_napis + '\n')

    zadanie_76_1()
    zadanie_76_2()
    zadanie_76_3()