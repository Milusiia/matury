import math

folder = 'infromatyka_arkusz_pliki/PLIKI DO ZADAN-arkusz II/dane.txt'
pomoc = 'infromatyka_arkusz_pliki/ODPOWIEDZI-arkusz II/Zadanie 4/pomoc.txt'

file_dane = open(folder)
dane = []

for element in file_dane:
    dane.append(int(element.replace("\n", "")))
# print(tablica)
file_dane.close()


def get_szczesliwe():
    liczby = list(range(1, 10001))
    for x in list(liczby):
        if x % 2 == 0:
            liczby.remove(x)

    index_usun = 1

    while index_usun < len(liczby):
        kolejna = liczby[index_usun]
        kopia_liczby = list(liczby)

        for idx in range(len(liczby)):
            element = liczby[idx]
            if (idx + 1) % kolejna == 0:
                kopia_liczby.remove(element)
        liczby = kopia_liczby
        index_usun += 1
    return liczby


def wykonaj1(lucky):
    suma = 0
    for liczba in dane:
        if liczba in lucky:
            suma += 1
    return suma


def check_operon_szczesliwe():
    file = open(pomoc)
    lines = file.readlines()[6:]
    szczesliwe_operon = []
    for line in lines:
        liczba, czy_szczesliwa = line.split()
        # print(liczba, czy_szczesliwa)
        if czy_szczesliwa == '0':
            szczesliwe_operon.append(int(liczba))
    return szczesliwe_operon


szczesliwe = get_szczesliwe()

# szczesliwe_operon = check_operon_szczesliwe()
print('len szczesliwe', len(szczesliwe))


# print('len szczesliwe_operon', len(szczesliwe_operon))
# print(len(szczesliwe_operon))
# print(wykonaj1(szczesliwe))
# print(wykonaj1(szczesliwe_operon))

def wykonaj2(lucky):
    max_dlugosc = 0
    max_pierwszy_element = -1

    aktualna_dlugosc = 0
    aktualnypierwszy = -1
    for x in dane:
        if x in lucky:
            aktualna_dlugosc += 1
            if aktualna_dlugosc == 1:
                aktualnypierwszy = x
            if aktualna_dlugosc > max_dlugosc:  # warunek gdy znajdujemy dłuższy ciąg
                max_dlugosc = aktualna_dlugosc
                max_pierwszy_element = aktualnypierwszy
        else:
            aktualna_dlugosc = 0

    return max_pierwszy_element, max_dlugosc


print(wykonaj2(szczesliwe))

"""
Niektóre z liczb szczęśliwych są również liczbami pierwszymi. Podaj, ile z podanych liczb to
jednocześnie liczba szczęśliwa i liczba pierwsza.
"""


def pierwsza(liczba):
    for x in range(2, int(math.sqrt(liczba) + 2)):
        if liczba % x == 0:
            return False
    return True


# list(print(f'Czy liczba {li} jest liczbą pierwszą: {pierwsza(li)}') for li in range(2, 50))

def zad3_czy_szczesliwe_pierwsze():
    suma = 0
    for y in dane:
        if y in szczesliwe and pierwsza(y):
            suma += 1
    return suma


print(f'Liczba szczesliwych i jednoczesnie pierwszych {zad3_czy_szczesliwe_pierwsze()}')
