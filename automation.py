f = open('inputFile.txt', 'r')
count = 0
for line in f:
    splitted_line = line.split()
    if splitted_line[2] == 'P':
        print(str(count) + ' ' + str(line))
    count = count + 1
f.close()