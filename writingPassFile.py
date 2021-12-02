f = open('inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
count = 0
for line in f:
    splitted_line = line.split()
    if splitted_line[2] == 'P':
        passFile.write(str(count) + ' ' + str(line))
    count = count + 1
f.close()
passFile.close()