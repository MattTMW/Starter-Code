from game_settings import *
partner1_uci_email_id = "mntruon4@uci.edu" # both partner's email IDs must be on each submission

import copy
copy_board = copy.deepcopy(board)

run = True
for row in copy_board:  # CREATES DEEP COPY OF BOARD AND ORGANIZES IT
    fixed_board = (' '.join(row))
    print(fixed_board)

def target_amount():
    amount_of_targets = 0
    for x in range(len(copy_board)):
        for y in range(len(copy_board[x])):
            if copy_board[x][y] == TARGET or copy_board[x][y] == BOX_S:
                amount_of_targets += 1
    return amount_of_targets

TARGETS = target_amount()

def win_con():
    dot_count = 0
    for x in range(len(copy_board)):
        for y in range(len(copy_board[x])):
            if copy_board[x][y] == BOX_S:
                dot_count += 1
    return dot_count == TARGETS


while run:
    if win_con():
        print('You Win!')
        break

    def find_sprite():                              # FINDING THE SPRITE
        for x in range(len(copy_board)):
            for y in range(len(copy_board[x])):
                if copy_board[x][y] == SPRITE or copy_board[x][y] == SPRITE_T:
                    return (x, y)


    def user_movements(movement):  #FUNCTION FOR MOVEMENTS


        if movement == 'a': #MOVE LEFT
            x, y = find_sprite()  # GETTING SPRITE LOCATION ON BOARD
            if copy_board[x][y - 1] == WALL:  # IF SPRITE HITS WALL
                pass
            elif copy_board[x][y - 1] == BOX_NS and copy_board[x][y - 2] == WALL:
                pass
            elif copy_board[x][y - 1] == BOX_NS and copy_board[x][y - 2] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x][y-1] == BOX_NS and copy_board[x][y-2] == BOX_S: #if there's a satisfied box next to exclamation and try to push that into it
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x][y - 1] == BOX_S and copy_board[x][y - 2] == BOX_NS:
                pass
            elif copy_board[x][y - 1] != WALL and copy_board[x][y - 1] == EMPTY and copy_board[x][y]==SPRITE:  # IF ITS NOT A WALL AND EMPTY IT'LL MOVE TO THE LEFT
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y] = EMPTY
            elif copy_board[x][y - 1] == BOX_NS and copy_board[x][y - 2] != TARGET and copy_board[x][y]==SPRITE:  # IF THE NEXT ONE IS AN EXCLAMATION POINT IT'LL MOVE THE EXCLAMATION POINT TOO
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y - 2] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y - 1] == BOX_NS and copy_board[x][y - 2] == TARGET and copy_board[x][y]==SPRITE:  # IF EXCLAMATION POINT LANDS ON A O THEN IT'LL BECOME .
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y - 2] = BOX_S
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE and copy_board[x][y - 1] == BOX_S and copy_board[x][y - 2] == WALL:
                pass
            elif copy_board[x][y - 1] == BOX_S:  # IF THE NEXT ONE IS . i BECOMES I and EXCLAMATION MARK MOVES RIGHT
                copy_board[x][y - 1] = SPRITE_T
                copy_board[x][y - 2] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x][y - 1] == BOX_NS and copy_board[x][y - 2] == TARGET:
                copy_board[x][y] = TARGET
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y - 2] = BOX_S
            elif copy_board[x][y] == SPRITE_T and copy_board[x][y - 1] == BOX_NS or copy_board[x][-1] == BOX_NS: #IF CURRENT POSITION = I and you move sprite to the right, then the ! moves to the right of sprite, and the space reverts to TARGET
                copy_board[x][y] = TARGET
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y - 2] = BOX_NS
            elif copy_board[x][y] == SPRITE and copy_board[x][y-1] == TARGET:    #IF SPRITE TRIES TO MOVE ON TO TARGET, IT BECOMES SPRITE_T
                copy_board[x][y-1] = SPRITE_T
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x][y - 1] == EMPTY: # IF SPRITE_T MOVES OFF OF THE TARGET IT CONVERST BACK INTO SPRITE
                copy_board[x][y - 1] = SPRITE
                copy_board[x][y] = TARGET





        elif movement == 'd':   # MOVE RIGHT
            x, y = find_sprite()          #GETTING SPRITE LOCATION ON BOARD
            if copy_board[x][y + 1] == WALL: #IF SPRITE HITS WALL
                pass
            elif copy_board[x][y + 1] == BOX_NS and copy_board[x][y + 2] == WALL: #IF SPRITE BEHIND AND EXCLAMATION POINT HITS WALL
                pass
            elif copy_board[x][y+1] == BOX_NS and copy_board[x][y+2] == BOX_NS: #IF TWO EXCLAMATION POINTS IN FRONT
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x][y + 1] == BOX_S and copy_board [x][y + 2] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x][y + 1] == BOX_NS and copy_board[x][y + 2] == BOX_S: #if there's a satisfied box next to exclamation and try to push that into it
                pass
            elif copy_board[x][y + 1] != WALL and copy_board[x][y+1] == EMPTY and copy_board[x][y]==SPRITE: #IF ITS NOT A WALL AND EMPTY IT'LL MOVE TO THE RIGHT AND ITS A SPRITE
                copy_board[x][y + 1] = SPRITE
                copy_board[x][y] = EMPTY
            elif copy_board[x][y + 1] == BOX_NS and copy_board[x][y+2] != TARGET and copy_board[x][y] == SPRITE: # IF THE NEXT ONE IS AN EXCLAMATION POINT IT'LL MOVE W EXCLAMATION POINT TOO
                copy_board[x][y + 1] = SPRITE
                copy_board[x][y + 2] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y + 1] == BOX_NS and copy_board[x][y+2] == TARGET and copy_board[x][y] == SPRITE:  #IF EXCLAMATION POINT LANDS ON A O THEN IT'LL BECOME .
                copy_board[x][y + 1] = SPRITE
                copy_board[x][y+2] = BOX_S
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE and copy_board[x][y+1] == BOX_S and copy_board[x][y+2] == WALL:
                pass
            elif copy_board[x][y + 1] == BOX_S: # IF THE NEXT ONE IS . i BECOMES I and EXCLAMATION MARK MOVES RIGHT
                copy_board[x][y + 1] = SPRITE_T
                copy_board[x][y + 2] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x][y + 1] == BOX_NS and copy_board[x][y + 2] == TARGET:
                copy_board[x][y] = TARGET
                copy_board[x][y + 1] = SPRITE
                copy_board[x][y +2] = BOX_S
            elif copy_board[x][y] == SPRITE_T and copy_board[x][y+1] == BOX_NS: #IF CURRENT POSITION = I and you move sprite to the right, then the ! moves to the right of sprite, and the space reverts to TARGET
                copy_board[x][y] = TARGET
                copy_board[x][y+1] = SPRITE
                copy_board[x][y+2] = BOX_NS
            elif copy_board[x][y] == SPRITE and copy_board[x][y+1] == TARGET:    #IF SPRITE TRIES TO MOVE ON TO TARGET, IT BECOMES SPRITE_T
                copy_board[x][y+1] = SPRITE_T
                copy_board[x][y] = EMPTY
            elif copy_board[x][y]==SPRITE_T and copy_board[x][y+1] == EMPTY: # IF SPRITE_T MOVES OFF OF THE TARGET IT CONVERST BACK INTO SPRITE
                copy_board[x][y+1] = SPRITE
                copy_board[x][y] = TARGET




        elif movement == 'w': # MOVING UP
            x, y = find_sprite()  # GETTING SPRITE LOCATION ON BOARD
            if copy_board[x - 1][y] == WALL:  # IF SPRITE HITS WALL
                pass
            elif copy_board[x - 1][y] == BOX_NS and copy_board[x - 2][y] == WALL:
                pass
            elif copy_board[x - 1][y] == BOX_NS and copy_board[x - 2][y] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x-1][y] == BOX_S and copy_board [x-2][y] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x - 1][y] == BOX_NS and copy_board[x - 2][y] == BOX_S: #if there's a satisfied box next to exclamation and try to push that into it
                pass
            elif copy_board[x - 1][y] != WALL and copy_board[x - 1][y] == EMPTY and copy_board[x][y]==SPRITE:  # IF ITS NOT A WALL AND EMPTY IT'LL MOVE TO THE RIGHT
                copy_board[x - 1][y] = SPRITE
                copy_board[x][y] = EMPTY
            elif copy_board[x - 1][y] == BOX_NS and copy_board[x - 2][y] != TARGET and copy_board[x][y]==SPRITE:  # IF THE NEXT ONE IS AN EXCLAMATION POINT IT'LL MOVE W EXCLAMATION POINT TOO
                copy_board[x - 1][y] = SPRITE
                copy_board[x - 2][y] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x - 1][y] == BOX_NS and copy_board[x - 2][y] == TARGET and copy_board[x][y]==SPRITE:  # IF EXCLAMATION POINT LANDS ON A O THEN IT'LL BECOME .
                copy_board[x - 1][y] = SPRITE
                copy_board[x - 2][y] = BOX_S
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE and copy_board[x - 1][y] == BOX_S and copy_board[x - 2] [y] == WALL: # WON'T WORK IF IT PUSHES INTO WALL
                pass
            elif copy_board[x - 1][y] == BOX_S:  # IF THE NEXT ONE IS . i BECOMES I and EXCLAMATION MARK MOVES RIGHT
                copy_board[x - 1][y] = SPRITE_T
                copy_board[x - 2][y] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] == TARGET:
                copy_board[x][y] = TARGET
                copy_board[x - 1][y] = SPRITE
                copy_board[x - 2][y] = BOX_S
            elif copy_board[x][y] == SPRITE_T and copy_board[x - 1][y] == BOX_NS:  # IF CURRENT POSITION = I and you move sprite to the right, then the ! moves to the right of sprite, and the space reverts to TARGET
                copy_board[x][y] = TARGET
                copy_board[x - 1][y] = SPRITE
                copy_board[x - 2][y] = BOX_NS
            elif copy_board[x][y] == SPRITE and copy_board[x-1][y] == TARGET:    #IF SPRITE TRIES TO MOVE ON TO TARGET, IT BECOMES SPRITE_T
                copy_board[x-1][y] = SPRITE_T
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x-1][y] == EMPTY: # IF SPRITE_T MOVES OFF OF THE TARGET IT CONVERST BACK INTO SPRITE
                copy_board[x-1][y] = SPRITE
                copy_board[x][y] = TARGET




        elif movement == 's':  # MOVING DOWN
            x, y = find_sprite()  # GETTING SPRITE LOCATION ON BOARD
            if copy_board[x + 1][y] == WALL:  # IF SPRITE HITS WALL
                pass
            elif copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] == WALL:
                pass
            elif copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x + 1][y] == BOX_S and copy_board [x + 2][y] == BOX_NS:
                pass
            elif copy_board[x][y] == SPRITE and copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] == BOX_S: #if there's a satisfied box next to exclamation and try to push that into it
                pass
            elif copy_board[x + 1][y] != WALL and copy_board[x + 1][y] == EMPTY and copy_board[x][y]==SPRITE:  # IF ITS NOT A WALL AND EMPTY IT'LL MOVE TO THE RIGHT
                copy_board[x + 1][y] = SPRITE
                copy_board[x][y] = EMPTY
            elif copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] != TARGET and copy_board[x][y]==SPRITE:  # IF THE NEXT ONE IS AN EXCLAMATION POINT IT'LL MOVE W EXCLAMATION POINT TOO
                copy_board[x + 1][y] = SPRITE
                copy_board[x + 2][y] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x + 1][y] == BOX_NS and copy_board[x + 2][y] == TARGET and copy_board[x][y]==SPRITE:  # IF EXCLAMATION POINT LANDS ON A O THEN IT'LL BECOME .
                copy_board[x + 1][y] = SPRITE
                copy_board[x + 2][y] = BOX_S
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE and copy_board[x+1][y] == BOX_S and copy_board[x + 2] [y] == WALL: # WON'T WORK IF IT PUSHES INTO WALL
                pass
            elif copy_board[x + 1][y] == BOX_S:  # IF THE NEXT ONE IS . i BECOMES I and EXCLAMATION MARK MOVES RIGHT
                copy_board[x + 1][y] = SPRITE_T
                copy_board[x + 2][y] = BOX_NS
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x+1][y] == BOX_NS and copy_board[x+2][y] == TARGET:
                copy_board[x][y] = TARGET
                copy_board[x+1][y] = SPRITE
                copy_board[x+2][y] = BOX_S
            elif copy_board[x][y] == SPRITE_T and copy_board[x + 1][y] == BOX_NS:  # IF CURRENT POSITION = I and you move sprite to the right, then the ! moves to the right of sprite, and the space reverts to TARGET
                copy_board[x][y] = TARGET
                copy_board[x + 1][y] = SPRITE
                copy_board[x + 2][y] = BOX_NS
            elif copy_board[x][y] == SPRITE and copy_board[x + 1][y] == TARGET:  # IF SPRITE TRIES TO MOVE ON TO TARGET, IT BECOMES SPRITE_T
                copy_board[x + 1][y] = SPRITE_T
                copy_board[x][y] = EMPTY
            elif copy_board[x][y] == SPRITE_T and copy_board[x + 1][y] == EMPTY:  # IF SPRITE_T MOVES OFF OF THE TARGET IT CONVERST BACK INTO SPRITE
                copy_board[x + 1][y] = SPRITE
                copy_board[x][y] = TARGET


        else:
            print()
            print('enter a valid move:', end='')

        if movement == 'a' or movement == 'w' or movement == 's' or movement == 'd':
            print()
            for row in copy_board:  # CREATES DEEP COPY OF BOARD AND ORGANIZES IT
                fixed_board = (' '.join(row))
                print(fixed_board)


    def new_board():                        #NEW BOARD IF USER PRESSES "SPACEBAR"
        copy_board = copy.deepcopy(board)
        return copy_board


    movement = input()
    if movement == 'q':
        print()
        print('Goodbye')
        break
    elif movement == ' ':
        copy_board = new_board()
        print()
        for row in copy_board:  # CREATES DEEP COPY OF BOARD AND ORGANIZES IT
            fixed_board = (' '.join(row))
            print(fixed_board)
    else:
        user_movements(movement)





