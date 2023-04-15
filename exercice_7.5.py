# Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2, n3 fournis en arguments.
# Par exemple, l’exécution de l’instruction : print(maximum(2,5,4)) doit donner le résultat:5.

def maximum(n1,n2,n3):
    "renvoie le plus grand de 3 nombres n1, n2, n3 fournis en arguments"
    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3
    return max

print(maximum(2,5,4))
print(maximum(5,4,4))
print(maximum(2,4,5))