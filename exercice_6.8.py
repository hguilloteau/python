# Programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 et de 5 compris entre ces bornes. Prendre par exemple a = 0, b=32;lerésultatdevraitêtrealors0+15+30=45.

a = 0
b = 30
somme = 0

while a <= b:
    a = a + 1
    if (a % 3 == 0) and (a % 5 == 0):
        somme = somme + a
print("Multiple de 3 et de 5, le total fait ", somme)

# Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et b. Avec les bornes 0 et 32, le résultat devrait donc être:0+3+ 5+6+9+10+12+15+18+20+21+24+25+27+30=225

a = 0
somme = 0
while a <= b:
    a = a + 1
    if (a % 3 == 0) or (a % 5 == 0):
        somme = somme + a
print("Multiple de 3 ou de 5, le total fait ", somme)
