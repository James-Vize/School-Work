#James Vize
#battleship


print('Welcome to BattleShip!')

boardSize = int(input('Enter the board size: '))
shipIndex = int(input('Enter the ship coordinate: '))
#create the board
is_found = False
board = []
for i in range(0, boardSize, 1):
    board.append('.')

#print the board
for i in range(0, boardSize, 1):
    print( f' {board[i]}', end= ' |')
print()

#print the grid numbers
for i in range(0, boardSize, 1):
    print( f' {i}', end= ' |')
print()



while is_found == False:

    #################
    #begin P2 turn
    #################
    guess = int(input('Player 2, Enter a guessed coordinate: '))

    if guess == shipIndex:
        is_found = True
        board[guess] = 'X'
    else:
        board[guess] = 'O'

    #print the board
    for i in range(0, boardSize, 1):
        print( f' {board[i]}', end= ' |')
    print()

    #print the grid numbers
    for i in range(0, boardSize, 1):
        print( f' {board[i]}', end= ' |')
    print()
    if is_found:
        print ('Hit! You sank my ship!')
    else:
        print ('Miss!')
