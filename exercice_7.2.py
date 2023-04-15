# fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca

def ligneCar(n, ca):
    "fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca"
    i = 0
    ch = ""
    while i < n:
        ch = ch + ca
        i = i + 1
    return ch

print(ligneCar(6,"a"))