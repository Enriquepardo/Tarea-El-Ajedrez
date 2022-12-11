

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


def imprimir_tablero_inicial():
    print('    a   b   c   d   e   f   g   h')
    print('  +---+---+---+---+---+---+---+---+')
    for i in range(8):
        print(i, end=' ')
        for j in range(8):
            print('|', tablero_ajedrez[(i,j)], end=' ')
        print('|', i)
        print('  +---+---+---+---+---+---+---+---+')
    print('    a   b   c   d   e   f   g   h')


def mover_ficha():
    print('Ingrese el movimiento de la ficha')
    print('Ejemplo: a2 a4')
    movimiento = input()
    return movimiento


def preguntar_movimientos():
    hacer_movimiento = input('¿Desea hacer un movimiento? (s/n): ')
    if hacer_movimiento == 's':
        mover_ficha()

def tablero_






def jugar ():
    imprimir_tablero_inicial()
    preguntar_movimientos()
