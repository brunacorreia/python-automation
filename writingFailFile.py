f = open('inputFile.txt', 'r')
failFile = open('failFile.txt', 'w')
count = 0
for line in f:
    splitted_line = line.split()
    if splitted_line[2] == "F":
        failFile.write(str(count) + ' ' + str(line))
    count += 1
f.close()
failFile.close()