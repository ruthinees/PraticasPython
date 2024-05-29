#Desenhar uma matriz com asteristicos

linhas = int(input('Digite o número de linhas da matriz: '))
colunas = int(input('Digite o número de colunas da matriz: '))

print('\n'f'Matriz[{linhas}][{colunas}]')

for i in range(linhas):
    for j in range(colunas):
        print('*', end = '')
    print()