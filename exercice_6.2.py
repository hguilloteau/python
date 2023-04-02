# programme qui calcule le périmètre et l’aire d’un triangle quelconque dont l’utilisateur fournit les 3 côtés. (Rappel: l’aire d’un triangle quelconque se calcule à l’aide de la formule: dans laquelle d désigne la longueur du demi-périmètre, et a, b, c celles des trois côtés.)

from math import sqrt
from math import *

a = input("Donner longueur du 1er côté du triangel : ")
b = input("Donner longueur du 2nd côté du triangel : ")
c = input("Donner longueur du 3ième côté du triangel : ")

perimetre = float(a) + float(b) + float(c)
p = perimetre / 2

print("Le périmètre de ce triangles est : ", perimetre)

aire = sqrt(p*(p-float(a))*(p-float(b))*(p-float(c)))

print("L'aire de ce triangle est de :",aire) 

# Correction

# # Périmètre et Aire d'un triangle quelconque
# print("Veuillez entrer le côté a : ")
# a = float(input())
# print("Veuillez entrer le côté b : ")
# b = float(input())
# print("Veuillez entrer le côté c : ")
# c = float(input())
# d = (a + b + c)/2  # demi-périmètre
# s = sqrt(d*(d-a)*(d-b)*(d-c))  # aire (suivant formule)
# print("Longueur des côtés =", a, b, c)
# print("Périmètre =", d*2, "Aire =", s)
