import random
from timeit import default_timer as timer


def generator(n):
    macierz = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(random.randint(0, 1))
        macierz.append(temp)
    return macierz


def pierwszy(macierz):
    n = len(macierz)
    maksimum = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(n - 1, x1 - 1, -1):
                for y2 in range(n - 1, y1 - 1, -1):
                    lokalne_maksimum = 0
                    for x in range(x1, x2 + 1):
                        for y in range(y1, y2 + 1):
                            lokalne_maksimum += macierz[x][y]
                    if lokalne_maksimum == (x2-x1+1)*(y2-y1+1) and lokalne_maksimum > maksimum:
                        maksimum = lokalne_maksimum
    return maksimum


def drugi(macierz):
    n = len(macierz)
    najwieksze_pole = 0
    for poziomy_index in range(0, n):
        for pionowy_indeks in range(0, n):
            # pom -> pomocniczy
            poziomy_pom = poziomy_index
            pionowy_maks = n - 1
            while poziomy_pom < n and macierz[poziomy_pom][pionowy_indeks] == 1:
                pionowy_pom = pionowy_indeks
                while pionowy_pom < (pionowy_maks + 1) and macierz[poziomy_pom][pionowy_pom] == 1:
                    pionowy_pom += 1
                pionowy_maks = pionowy_pom - 1
                l_najwieksze_pole = (poziomy_pom - poziomy_index + 1) * (pionowy_maks - pionowy_indeks + 1)
                if l_najwieksze_pole > najwieksze_pole:
                    najwieksze_pole = l_najwieksze_pole
                poziomy_pom += 1
    return najwieksze_pole


nn = [20, 40, 80, 160, 320]

for n in nn:
    start = timer()
    pierwszy(generator(n))
    stop = timer()
    Tn = stop - start
    Fn = n**6
    print(n, Tn, Fn / Tn)

# pierwszy
# złożoność: n**6
# 20 0.1953074 327688556.6035901
# 40 8.873407799999999 461603939.8076577
# 50 32.90162479999999 474900558.71040154
# 60 95.58785690000002 488095470.6287592
# 70 240.05826880000004 490085180.5193056
# 80 526.6962899 497713777.421465

# drugi
# złożoność: n**3
# 500 0.3333964 749858.1268424015
# 1000 1.2684834999999999 788342.9307515628
# 2000 5.0732683 788446.3748940699
# 4000 20.869391200000003 766673.0594421938
# 8000 82.47967220000001 775948.7676528374
