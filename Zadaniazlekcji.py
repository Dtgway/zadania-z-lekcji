
from math import pi as PI
import time
import random

#wersja 1 zadanie 1

print("Obliczanie pola kuli")
r = float(input("r = "))
print(f"Pole kuli dla r = {r} = {4*PI*r}")

#wersja 1 zadanie 2

n = int(input("ile razy - "))
while 0 < n:
    print("kocham programowac")
    n -= 1

#wersja 1 zadanie 3

suma = 0
while True:
    inp = input("Podaj liczbe ktora chcesz zsumowac lub stop jesli chcesz zakonczyc  ")

    if inp == "stop":
        break

    liczba = float(inp)
    suma += liczba
print(f"suma tych liczb wynosi {suma}")

#wersja 1 zadanie 4


ile = 0
suma = 0
while True:
    inp = input("Podaj liczby ktorych srednia chesz sprawdzic  ")

    if inp == "stop":
        break
    ile += 1
    liczba = float(inp)
    suma += liczba

print(f"srednia tych liczb wynosi {suma/ile}")


#wersja 1 zadanie 5a


suma = 0
n = int(input("Ile poteg liczby 2 - "))
i = 0
while n > 0:
    i += 1
    n -= 1
    suma += 2**i
print(f"Suma pierwszych {i} poteg liczby 2 = {suma}")


#wersja 2 zadanie 1


print("Obliczanie objetosci ostroslupa")
pp = float(input("pp = "))
h = float(input("h = "))
print(f"objetosc ostroslupa dla pp = {pp} i h = {h} = {1/3*pp*h}")


#wersja 2 zadanie 2


liczba = random.randint(1,100)
proby = 3
wygrana = False
print("gra w zgadywanie liczby od 1 do 100")
while proby > 0 and not wygrana:
    traf = int(input(f"proba {4-proby}. Zgaduj!  "))
    if traf == liczba:
        wygrana = True
        print("Masz farta, nastepnym razem ci sie nie uda")
    else:
        proby -= 1
        if proby > 0:
            print(f"Zostalo ci jeszcze {proby} prob ale i tak ci sie nie uda")
    if not  wygrana and proby == 0:
        print("I tak nigdy nie miales szans!")


#wersja 2 zadanie 3

najwieksza = None
n = int(input("n = "))
while n > 0:
    z = input("Liczby - ")
    
    
    i = float(z)
    if najwieksza == None or i > najwieksza:
        najwieksza = i
    n -= 1
    print(i)
i = 0
while True:
    chcesz = input("wyswietlic? - ")
    if chcesz == "stop":
        break
print(najwieksza)


#wersja 2 zadanie 4

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("Mozna zbudowac trojkat prostokatny")
else:
    print("nie mozna zbudowac trojkata prostokatnego")


#wersja 2 zadanie 5











#wesja 3 zadanie 1



print("obliczanie objetosci szescianu")
a = float(input("a = "))
print(f"objetosc szescianu dla a = {a} = {a*a*a}")




#wersja 3 zadanie 2



i = 10
while i > 0:
    x = random.randint(1,10000)
    print(x)
    i -= 1
    time.sleep(0.1)


#wersja 3 zadanie 3

ile = 0
suma = 0
while True:
    inp = input("Podaj liczbe ktora chcesz zsumowac lub stop jesli chcesz zakonczyc  ")

    if inp == "stop":
        break

    liczba = float(inp)
    suma += liczba
    ile += 1
print(f"suma tych liczb wynosi {suma}")
print(f"srednia tych liczb wynosi {suma/ile}")



#wersja 3 zadanie 4


prostokatny = False
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    prostokatny = True
elif prostokatny == True and a == b or a == c or b == c:
    print("prostokatny rownoramienny")
elif prostokatny == False and a == b == c:
    print("rownoboczny")

else:
    print("nie mozna zbudowac trojkata prostokatnego")



#wersja 3 zadanie 5



k = float(input("k = "))
m = float(input("m = "))
print(f"reszta z dzielenia {k} przez {m} = {k % m}")




#wersja 3 zadanie 6



k = float(input("k = "))
m = float(input("m = "))

print(f"Liczba k dzieli sie przez m {k/m} razy")