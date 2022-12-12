import os


fichas_negras = ['♜', '♞', '♝',	'♛'	, '♚', '♝',	'♞', '♜', '♟', '♟',	'♟', '♟', '♟', '♟', '♟', '♟']
fichas_blancas = ['♖', '♘', '♗', '♕', '♔', '♗',	'♘', '♖', '♙', '♙',	'♙', '♙', '♙', '♙', '♙', '♙']

tablero_ajedrez = {
    (0,0): fichas_blancas[0], (0,1): fichas_blancas[1], (0,2): fichas_blancas[2], (0,3): fichas_blancas[3], (0,4): fichas_blancas[4], (0,5): fichas_blancas[5], (0,6): fichas_blancas[6], (0,7): fichas_blancas[7],
    (1,0): fichas_blancas[8], (1,1): fichas_blancas[9], (1,2): fichas_blancas[10], (1,3): fichas_blancas[11], (1,4): fichas_blancas[12], (1,5): fichas_blancas[13], (1,6): fichas_blancas[14], (1,7): fichas_blancas[15],
    (2,0): ' ', (2,1): ' ', (2,2): ' ', (2,3): ' ', (2,4): ' ', (2,5): ' ', (2,6): ' ', (2,7): ' ',
    (3,0): ' ', (3,1): ' ', (3,2): ' ', (3,3): ' ', (3,4): ' ', (3,5): ' ', (3,6): ' ', (3,7): ' ',
    (4,0): ' ', (4,1): ' ', (4,2): ' ', (4,3): ' ', (4,4): ' ', (4,5): ' ', (4,6): ' ', (4,7): ' ',
    (5,0): ' ', (5,1): ' ', (5,2): ' ', (5,3): ' ', (5,4): ' ', (5,5): ' ', (5,6): ' ', (5,7): ' ',
    (6,0): fichas_negras[8], (6,1): fichas_negras[9], (6,2): fichas_negras[10], (6,3): fichas_negras[11], (6,4): fichas_negras[12], (6,5): fichas_negras[13], (6,6): fichas_negras[14], (6,7): fichas_negras[15],
    (7,0): fichas_negras[0], (7,1): fichas_negras[1], (7,2): fichas_negras[2], (7,3): fichas_negras[3], (7,4): fichas_negras[4], (7,5): fichas_negras[5], (7,6): fichas_negras[6], (7,7): fichas_negras[7]
}

nombre_fichero = input('Ingrese el nombre del fichero, donde se van a guardar los movimientos: \n')


print('--------Este es el tablero inicial del ajedrez:--------')
fichero = open(nombre_fichero, 'w')

def tablero_fichero():
    fichero = open(nombre_fichero, 'a')
    fichero.write('--------Este es el tablero inicial del ajedrez:--------')
    fichero.write('    0   1   2   3   4   5   6   7')
    fichero.write('  +---+---+---+---+---+---+---+---+')
    fichero.write('')
    for i in range(8):
        for j in range(8):
            fichero.write(tablero[i][j]+'\t')
        fichero.write('|' + str(i))
        fichero.write('  +---+---+---+---+---+---+---+---+')
    fichero.write('    0   1   2   3   4   5   6   7')
    fichero.close()
    
    
def imprimir_tablero_inicial():
    print('    0   1   2   3   4   5   6   7')
    print('  +---+---+---+---+---+---+---+---+')
    for i in range(8):
        print(i, end=' ')
        for j in range(8):
            print('|', tablero_ajedrez[(i,j)], end=' ')
        print('|', i)
        print('  +---+---+---+---+---+---+---+---+')
    print('    0   1   2   3   4   5   6   7')
      
    
    
def preguntar_movimientos():
    hacer_movimiento = input('¿Desea hacer un movimiento? (s/n): ')
    if hacer_movimiento == 's':
        mover_ficha()
    elif hacer_movimiento == 'n':
        print('Gracias por jugar!')
        fichero.close()
        os._exit(0)
    else:
        print('Por favor, ingrese una opción válida.')
        preguntar_movimientos()
        
        
def mover_ficha():
    print('Ingrese el movimiento de la ficha:')
    fila_ficha = int(input('Ingrese la fila de la ficha: '))
    columna_ficha = int(input('Ingrese la columna de la ficha: '))
    print('La ficha que desea mover es: ', tablero_ajedrez[(fila_ficha, columna_ficha)])
    
    movimiento_fila = int(input('Ingrese la fila a la que desea mover la ficha: '))
    movimiento_columna = int(input('Ingrese la columna a la que desea mover la ficha: '))
    
    tablero_ajedrez[movimiento_fila, movimiento_columna] = tablero_ajedrez[(fila_ficha, columna_ficha)]
    tablero_ajedrez[fila_ficha, columna_ficha] = ' '
    
    print('\n--------Este es el tablero actualizado:--------')
    imprimir_tablero_inicial()
  
    fichero = open(nombre_fichero, 'a', encoding= 'utf-8')
    fichero.write('La ficha que se movió fue:  {}'.format(tablero_ajedrez[(fila_ficha, columna_ficha)]))
    fichero.write('La ficha fue movida a la posición:  {}'.format(tablero_ajedrez[(movimiento_fila, movimiento_columna)]))
    fichero.close()



def jugar():
    imprimir_tablero_inicial()
    while True:
        preguntar_movimientos()
        mover_ficha()
        if tablero_ajedrez[(0,0)] == ' ' and tablero_ajedrez[(0,1)] == ' ' and tablero_ajedrez[(0,2)] == ' ' and tablero_ajedrez[(0,3)] == ' ' and tablero_ajedrez[(0,4)] == ' ' and tablero_ajedrez[(0,5)] == ' ' and tablero_ajedrez[(0,6)] == ' ' and tablero_ajedrez[(0,7)] == ' ':
            print('Ganó el jugador 2')
            
            fichero.close()
            os._exit(0)
        if tablero_ajedrez[(7,0)] == ' ' and tablero_ajedrez[(7,1)] == ' ' and tablero_ajedrez[(7,2)] == ' ' and tablero_ajedrez[(7,3)] == ' ' and tablero_ajedrez[(7,4)] == ' ' and tablero_ajedrez[(7,5)] == ' ' and tablero_ajedrez[(7,6)] == ' ' and tablero_ajedrez[(7,7)] == ' ':
            print('Ganó el jugador 1')
            
            fichero.close()
            os._exit(0)
    
