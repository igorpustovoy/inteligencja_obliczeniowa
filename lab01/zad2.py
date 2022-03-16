from math import *
from random import *
from statistics import *


def suma(l1, l2):
    l3 = []
    for i in range(0, len(l1)):
        l3.append(l1[i] + l2[i])
    return l3


def iloczyn(l1, l2):
    l3 = []
    for i in range(0, len(l1)):
        l3.append(l1[i] * l2[i])
    return l3


def iloczyn_skalarny(l1, l2):
    iloczyn = 0
    for i in range(0, len(l1)):
        iloczyn += (l1[i] * l2[i])
    return iloczyn


def dlugosc_euklidesowa(l1):
    suma = 0
    for i in l1:
        suma += i * i
    return sqrt(suma)


def losowy_wektor():
    random_list = []
    for i in range(0, 50):
        random_list.append(randint(0, 100))
    return random_list

def mean(l1):
    suma = 0
    for number in l1:
        suma += number
    return suma / len(l1)

def min(l1):
    minimum = l1[0]
    for number in l1:
        if number < minimum:
            minimum = number
    return minimum

def max(l1):
    maximum = l1[0]
    for number in l1:
        if number > maximum:
            maximum = number
    return maximum


def standard_devation(l1):
    return stdev(l1)


def normalisation(l1):
    maxi = max(l1)
    mini = min(l1)
    index = 0
    new_list = []
    for i in range(0, len(l1)):
        new_list.append((l1[i] - mini) / (maxi - mini))
        if l1[i] == maxi:
            index = i
    print(f"Maximum oryginalnej listy to {maxi} na indexie {index}, nowa wartość na tym indexie to: {new_list[index]}")
    return new_list


def standarisation(l1):
    list_mean = mean(l1)
    stdeviation = stdev(l1)
    new_list = []
    for number in l1:
        new_list.append((number - list_mean) / stdeviation)
    print(f"Nowy wektor ma średnią wynoszącą: {mean(new_list)}, a odchylenie standardowe równe: {stdev(new_list)}")
    return new_list


def discretization(l1):
    l2 = []
    for number in l1:
        bottom = 0
        ceiling = 100
        for i in range(0, 101, 10):
            if i > number:
                bottom = i - 10
                break
            elif i == number:
                bottom = i
                break
        for i in range(0, 101, 10):
            if i > number:
                ceiling = i
                break
        l2.append(f"[{bottom}, {ceiling})")
    return l2



A = [3, 8, 9, 10, 12]
B = [8, 7, 7, 5, 6]

# Zad 2 a)
print("Zad 2 a)")
print(f"Suma dwóch wektorów to: {suma(A, B)}")
print(f"Iloczyn dwóch wektorów to: {iloczyn(A, B)}")

# Zad 2 b)
print("Zad 2 b)")
print(f"Iloczyn skalarny dwóch wektorów to: {iloczyn_skalarny(A, B)}")

# Zad 2 c)
print("Zad 2 c)")
print(f"Długość euklidesowa dla pierwszego wektora: {dlugosc_euklidesowa(A)}")
print(f"Długość euklidesowa dla drugiego wektora: {dlugosc_euklidesowa(B)}")

# Zad 2 d)
print("Zad 2 d)")
random_matrix = losowy_wektor()
print(f"Losowa macierz to: {random_matrix}")

# Zad 2 e)
print("Zad 2 e)")
print(f"Średnia z losowego wektora to: {mean(random_matrix)}")
print(f"Minimum z losowego wektora to: {min(random_matrix)}")
print(f"Maximum z losowego wektora to: {max(random_matrix)}")
print(f"Odchylenie standardowe z losowego wektora to: {standard_devation(random_matrix)}")

# Zad 2 f)
print("Zad 2 f)")
print(f"Wektor losowy po normalizacji: {normalisation(random_matrix)}")

# Zad 2 g)
print("Zad 2 g)")
print(f"Wektor losowy po standaryzacji: {standarisation(random_matrix)}")

# Zad 2 h)
print("Zad 2 h)")
print(f"Wektor losowy po dyskretyzacji: {discretization(random_matrix)}")



