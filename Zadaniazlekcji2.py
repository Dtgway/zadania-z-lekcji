# from random import randint

#zadanie 1

x = []
while len(x) != 10:
    x.append(randint(1,101))
print(x)


#zadanie 2

z = []
while len(z) != 20:
    k = randint(100,201)
    if k % 2 == 0 and k % 5 != 0:
        z.append(k)
print(z)


#zadanie 3

d = 0
v = 0
b = 0
n = 0
k = 0
zdanie = input("napisz dowolne zdanie -----  ")
licz = list(zdanie)
for el in licz:
    if el  == 'd':
        d += 1
    if el  == 'v':
            v += 1
    if el == 'b':
            b += 1
    if el == 'n':
            n += 1
    if el == 'k':
            k += 1
print(f"W twoim zdaniu jest {d} d, {v} v, {b} b, {n} n i {k} k")
print(licz)




#zadanie 5

mniejszeod0 = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el < 0:
        mniejszeod0 += 1
print("===============================")
print(mniejszeod0)



#zadanie 6

mniejszerowne = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el > 0 or el == 0:
        mniejszerowne += 1
print("=================================")
print(mniejszerowne)




#zadanie 7 


suma = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el % 2 == 0:
        suma += el
print("====================================")
print(suma)




#zadanie 8



suma = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el % 2 != 0:
        suma += el
print("====================================")
print(suma)




#zadanie 9


suma = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el % 5 == 0 and el % 7 == 0:
        suma += el
print("====================================")
print(suma)



#zadanie 10


ile = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
liczba = int(input("Napisz jaka liczbe z listy chcesz policzyc (od -50 do 50) ----   "))
for el in lista:
    if el == liczba:
        ile += 1
print("=======================================")
print(ile)




#zadanie 11




index = 0
najw = 0
najwindex = 0
najm = 0
najmindex = 0
from random import randint
lista = [randint(-50,50) for el in range(100)]
print(lista)
for el in lista:
    if el > najw:        
        najw = el        
        najwindex = index
    if el < najm:
        najm = el
        najmindex = index
    index += 1
print("=================================================")
print(f"Najwieksza liczba to {najw} a jej index = {najwindex}, najmniejsza liczba to {najm} a jej index = {najmindex}")



#zadanie 12



zasieg = int(input("od jakiej liczby chcesz zaczac liste (jaka tylko sobie wymarzysz liczba calkowita) -----   "))
zasiegk = int(input("do jakiej liczby chcesz liste (jaka tylko sobie wymarzysz liczba calkowita) -----   "))
if zasieg > zasiegk or zasieg == zasiegk:
    print("Liczba od ktorej zaczynasz liste musi byc mniejsza od tej ktora konczysz")
    zasieg = int(input("od jakiej liczby chcesz zaczac liste (jaka tylko sobie wymarzysz liczba calkowita) -----   "))
wielkosc = int(input("ile liczb ma miec twoja lista --------    "))


from random import randint
lista = [randint(zasieg,zasiegk) for el in range(wielkosc)]
print(lista)


    