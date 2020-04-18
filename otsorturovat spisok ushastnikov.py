inFile = open('input.txt', 'r', encoding='utf-8')
matrix = []
for line in inFile:
    line = line.split()
    line.pop(2)
    matrix.append(line)
inFile.close()
matrix.sort()
for i in matrix:
    for j in i:
        print(j, end=' ')
    print()
