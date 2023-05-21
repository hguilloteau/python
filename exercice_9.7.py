# À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne al- ternativement un élément de A, un élément de B, un élément de A... et ainsi de suite jusqu’à atteindre la fin de l’un des deux fichiers originaux. Complétez ensuite C avec les éléments restant sur l’autre.

filename1 = 'Monfichier.txt'
filename2 = 'Monfichierdiff.txt'
filename3 = 'Monfichierfusion.txt'
file1 = open(filename1, 'r')
file2 = open(filename2, 'r')
file3 = open(filename3, 'w')

while 1:
    line1 = file1.readline()
    line2 = file2.readline()
    if line1 == '' and line2 == '':
        break
    elif line1 == '':
        file3.write(line2)
    elif line2 == '':
        file3.write(line1)
    else:
        file3.write(line1)
        file3.write(line2)

file1.close()
file2.close()
file3.close()