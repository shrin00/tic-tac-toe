from itertools import cycle

# check wether all items are same
def all_same(l):
    #list.count(x) returns number of occurence of 'x' in the list
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    return False


def win(current_game, player):
    # horizontal win
    for row in current_game:
        if all_same(row):
            print(f'player \'{player}\' is the winner!!....Horizontally(--)')
            return True
    
    # vertical win
    for i in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[i])
        if all_same(check):
            print(f'player \'{player}\' is the winner!!....Vertically(|)')
            return True

    # diagonal win 1
    diags = []
    for idx in range(len(current_game)):
        diags.append(current_game[idx][idx])
    if all_same(diags):
        print(f'player \'{player}\' is the winner!!.....Diagonally(\)')
        return True

    # diagonal win 2
    diags = []
    for row, col in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
    if all_same(diags):
        print(f'player \'{player}\' is the winner!!......Diagonally(/)')
        return True  
    return False


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("   "+"  ".join([str(x) for x in range(len(game_map))]))
        if not just_display:
                game_map[row][col] = player

        for count, row in enumerate(game_map):
                print(count, row) 
        return game_map

    except IndexError as e:
        print("Make sure to enter 0, 1, or 2...!", e)

    except Exception as e:
        print("Something went wrong....!", e)


def check_game_status(game_map):
    for row in game_map:
        for x in row:
            if x == 0:
                return False
    return True


play = True
player = cycle([1,2])
while play:
    game_size = int(input("Please enter the game size '>=3': "))
    if game_size >= 3:
        game = [[0 for x in range(game_size)] for y in range(game_size)]
        game_won = False
        game = game_board(game, just_display=True) 
        while not game_won:
            current_player = next(player)
            print(f'current player: {current_player}')
            played = False
            while not played:
                try:
                    row = int(input(f'choose the row{[x for x in range(len(game))]}: '))
                    col = int(input(f'choose the coloumn{[x for x in range(len(game))]}: '))
                    if row < len(game) and col < len(game):
                        if game[row][col] == 0:
                            game = game_board(game, current_player, row, col)
                            played = True
                            game_won = win(game, current_player)
                        else:
                            print(f'{[row, col]} this position has been played!..Please play another position..')
                    else:
                        print(f'please select only between {[x for x in range(len(game))]}')  
                except:
                    print("please enter numbers only...")
            # check all the position played and yet winner is not decided
            if check_game_status(game):
                game_won = True
                print("Game has ended and it is a 'DRAW'.......")
        
        choose = input("Game has ended!!! Do you want play again(y/n): ")
        if choose.lower() != 'y':
            print("You played a good game!!! See you again...")
            play = False