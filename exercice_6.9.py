# Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non. Une année A est bissextile si A est divisible par 4. Elle ne l’est cependant pas si A est un multiple de 100, à moins que A ne soit multiple de 400.

A = eval(input("Entrer une année ? "))

if (A%4==0) and ((A%100) or (A%400==0)):
    print("L'année",A,"est bissextile")
else:
    print("L'année",A,"n'est pas bissextile")