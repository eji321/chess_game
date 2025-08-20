chess_board = [['a8','b8','c8','d8','e8','f8','g8','h8'],
               ['a7','b7','c7','d7','e7','f7','g7','h7'],
               ['a6','b6','c6','d6','e6','f6','g6','h6'],
               ['a5','b5','c5','d5','e5','f5','g5','h5'],
               ['a4','b4','c4','d4','e4','f4','g4','h4'],
               ['a3','b3','c3','d3','e3','f3','g3','h3'],
               ['a2','b2','c2','d2','e2','f2','g2','h2'],
               ['a1','b1','c1','d1','e1','f1','g1','h1']]

game_state = [['r1','n1','b1','q','k','b2','n2','r2'],
                   ['p1','p2','p3','p4','p5','p6','p7','p8'],
                   ['X','X','X','X','X','X','X','X'],
                   ['X','X','X','X','X','X','X','X'],
                   ['X','X','X','X','X','X','X','X'],
                   ['X','X','X','X','X','X','X','X'],
                   ['P1','P2','P3','P4','P5','P6','P7','P8'],
                   ['R1','N1','B1','Q','K','B2','N2','R2']]

captured_pieces = []

def print_board(board_list):
    for j in range(len(board_list)):
        print("\n")
        for i in range(len(board_list[j])):
            if 1 < j < 6:
                print(board_list[j][i], end="  ")
            else:
                print(board_list[j][i], end=" ")
    print('\n')


def is_game_over(capture_list):
    if len(capture_list) == 0:
        return True
    elif len(capture_list) > 0:
        for i in range(len(capture_list)):
            if capture_list[i] == 'K' or capture_list[i] == 'k':
                return False
        return True


def find_piece(piece):
    for j in range(len(game_state)):
        for i in range(len(game_state[j])):
            if game_state[j][i] == piece:
                return i,j
    return False


def find_square(square):
    for b in range(len(chess_board)):
        for a in range(len(chess_board[b])):
            if chess_board[b][a] == square:
                return b,a
    print("Square not found")
    return False

def is_piece_available(piece):
    if find_piece(piece) != False:
        return True
    else:
        print("This piece has been captured!")
        return False







class piece:
    def __init__(self,name,color,position):
        self.name = name
        self.color = color
        self.position = position

    def valid_moves(self):
        #returns a list of all possible moves for the piece

class pawn(piece):




while is_game_over(captured_pieces):
    print_board(game_state)


    piece_type = input("Which piece type are you playing?: ")
    chosen_piece = input("Pick a piece: ")
    # an if statement using the is_piece_available function. If piece has been captured, as for another piece as input
    move_or_capture = input("Are move moving a piece or capturing an opponent piece (m/c) ?: ")
    # an if statement to ask for final move position or position of capture
    final_position = input("Which square will you place " + chosen_piece + "?: ")
    capture_position = input("Which square are you attacking?: ")


print("GAME OVER")



