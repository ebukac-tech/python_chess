import pygame
from sys import exit
import os
import math

#pictures

LightBishop = pygame.transform.scale(pygame.image.load("pictures//LightBishop.png"), (80,80))
rect_LightBishop = LightBishop.get_rect()
 
DarkBishop = pygame.transform.scale(pygame.image.load("pictures//DarkBishop.png"), (80,80))
rect_DarkBishop = DarkBishop.get_rect()
 
LightQueen = pygame.transform.scale(pygame.image.load("pictures//LightQueen.png"), (80,80))
rect_LightQueen = LightQueen.get_rect()
 
LightKing = pygame.transform.scale(pygame.image.load("pictures//LightKing.png"), (80,80))
rect_LightKing = LightKing.get_rect()
 
DarkKing = pygame.transform.scale(pygame.image.load("pictures//DarkKing.png"), (80,80))
rect_DarkKing = DarkKing.get_rect()
 
DarkQueen = pygame.transform.scale(pygame.image.load("pictures//DarkQueen.png"), (80,80))
rect_DarkQueen = DarkQueen.get_rect()
 
LightKnight = pygame.transform.scale(pygame.image.load("pictures//LightKnight.png"), (80,80))
rect_LightKnight = LightKnight.get_rect()
 
LightRook = pygame.transform.scale(pygame.image.load("pictures//LightRook.png"), (80,80))
rect_LightRook = LightRook.get_rect()
 
DarkRook = pygame.transform.scale(pygame.image.load("pictures//DarkRook.png"), (80,80))
rect_DarkRook = DarkRook.get_rect()
 
DarkKnight = pygame.transform.scale(pygame.image.load("pictures//DarkKnight.png"), (80,80))
rect_DarkKnight = DarkKnight.get_rect()
 
DarkPawn = pygame.transform.scale(pygame.image.load("pictures//DarkPawn.png"), (80,80))
rect_DarkPawn = DarkPawn.get_rect()
 
LightPawn = pygame.transform.scale(pygame.image.load("pictures//LightPawn.png"), (80,80))
rect_LightPawn = LightPawn.get_rect()



class Piece:
    def __init__(self, colour, pieceType):
        self.colour = colour
        self.pieceType = pieceType


    

class Square:
    def __init__(self, file, rank):
        self.file = file
        self.rank = rank
        self.piece = None

    def remove_pieces(self):
        self.piece = None

    def receive_pieces(self, moved_piece):
        self.piece = moved_piece
  
board = [[Square(file, rank) for file in range(8)] for rank in range(8)]

#the piece attribute of the square class is declared as an intance of the piece class

board[0][0].piece = Piece('w', 'R')
board[0][1].piece = Piece('w', 'N')
board[0][2].piece = Piece('w', 'B')
board[0][3].piece = Piece('w', 'Q')
board[0][4].piece = Piece('w', 'K')
board[0][5].piece = Piece('w', 'B')
board[0][6].piece = Piece('w', 'N')
board[0][7].piece = Piece('w', 'R')

board[7][0].piece = Piece('b', 'R')
board[7][1].piece = Piece('b', 'N')
board[7][2].piece = Piece('b', 'B')
board[7][3].piece = Piece('b', 'Q')
board[7][4].piece = Piece('b', 'K')
board[7][5].piece = Piece('b', 'B')
board[7][6].piece = Piece('b', 'N')
board[7][7].piece = Piece('b', 'R')

board[1][0].piece = Piece('w', 'P')
board[1][1].piece = Piece('w', 'P')
board[1][2].piece = Piece('w', 'P')
board[1][3].piece = Piece('w', 'P')
board[1][4].piece = Piece('w', 'P')
board[1][5].piece = Piece('w', 'P')
board[1][6].piece = Piece('w', 'P')
board[1][7].piece = Piece('w', 'P')

board[6][0].piece = Piece('b', 'P')
board[6][1].piece = Piece('b', 'P')
board[6][2].piece = Piece('b', 'P')
board[6][3].piece = Piece('b', 'P')
board[6][4].piece = Piece('b', 'P')
board[6][5].piece = Piece('b', 'P')
board[6][6].piece = Piece('b', 'P')
board[6][7].piece = Piece('b', 'P')


print(board[7][0].piece)

def draw_board():
    square_size = 80
    
    for rank in range(8):
        for file in range(8):
            if (file + rank) % 2 == 0:
                pygame.draw.rect(screen, "LightGray", (file*80, rank*80, square_size, square_size))
            else:
                pygame.draw.rect(screen, "LightSeaGreen", (file*80, rank*80,square_size, square_size))


    
            center_x = file*square_size + square_size//2
            center_y = rank*square_size + square_size//2
            if board[rank][file].piece != None:
                if board[rank][file].piece.colour == 'b':
                    if board[rank][file].piece.pieceType == 'R':
                        rect_DarkRook.center = (center_x,center_y)
                        screen.blit(DarkRook, rect_DarkRook)
                    elif board[rank][file].piece.pieceType == 'N':
                        rect_DarkKnight.center = (center_x,center_y)
                        screen.blit(DarkKnight, rect_DarkKnight)
                    elif board[rank][file].piece.pieceType == 'B':
                        rect_DarkBishop.center = (center_x,center_y)
                        screen.blit(DarkBishop, rect_DarkBishop)
                    elif board[rank][file].piece.pieceType == 'Q':
                        rect_DarkQueen.center = (center_x,center_y)
                        screen.blit(DarkQueen, rect_DarkQueen)
                    elif board[rank][file].piece.pieceType == 'K':
                        rect_DarkKing.center = (center_x,center_y)
                        screen.blit(DarkKing, rect_DarkKing)
                    elif board[rank][file].piece.pieceType == 'P':
                        rect_DarkPawn.center = (center_x, center_y)
                        screen.blit(DarkPawn, rect_DarkPawn)
                elif board[rank][file].piece.colour == 'w':
                    if board[rank][file].piece.pieceType == 'R':
                        rect_LightRook.center = (center_x,center_y)
                        screen.blit(LightRook, rect_LightRook)
                    elif board[rank][file].piece.pieceType == 'N':
                        rect_LightKnight.center = (center_x,center_y)
                        screen.blit(LightKnight, rect_LightKnight)
                    elif board[rank][file].piece.pieceType == 'B':
                        rect_LightBishop.center = (center_x,center_y)
                        screen.blit(LightBishop, rect_LightBishop)
                    elif board[rank][file].piece.pieceType == 'Q':
                        rect_LightQueen.center = (center_x,center_y)
                        screen.blit(LightQueen, rect_LightQueen)
                    elif board[rank][file].piece.pieceType == 'K':
                        rect_LightKing.center = (center_x,center_y)
                        screen.blit(LightKing, rect_LightKing)
                    elif board[rank][file].piece.pieceType == 'P':
                        rect_LightPawn.center = (center_x,center_y)
                        screen.blit(LightPawn, rect_LightPawn)


def side_panel(last_move, colour):
    panel_rect = (640,0,300,740)
    pygame.draw.rect(screen, "Gray", panel_rect)
    panel_font = pygame.font.Font(None, 25)
    panel_txt_surface = panel_font.render("Moves: ", True, colour)
    sidePanel_txt_surface = panel_font.render(", ".join(last_move), True, colour)
    screen.blit(sidePanel_txt_surface, (645+6, 30))
    screen.blit(panel_txt_surface, (645+6, 15))

def input_box():
    #input box
    box_rect = (0,640,640,100)
    pygame.draw.rect(screen, "CadetBlue", box_rect)
    input_txt_label = font.render("Input Box: ", True, colour)
    input_txt_surface = font.render(text, True, colour)
    screen.blit(input_txt_surface, (200+5, 645+6)) #text pos
    screen.blit(input_txt_label, (5, 645+6))
    pygame.draw.rect(screen, colour, (200, 645, 200, 50), 2) # drawing box around text #805 for 645


pygame.init()

#creating screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((900,740), pygame.RESIZABLE)
pygame.display.set_caption("Chess Game")

#for side panel
font = pygame.font.Font(None, 50) # use a default font to draw text at size 32
colour = pygame.Color('black')
text = ''
last_move = []

# for moving pieces
selected = False
selectedPiecePos_x = None
selectedPiecePos_y = None

#for captured pieces
white_captured_pieces = []
black_captured_pieces = []

while True:
    for event in pygame.event.get():
        # enables window to be closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if selected == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                currentMouse_pos = pygame.mouse.get_pos()
                selectedPiecePos_x = math.floor(currentMouse_pos[0]//80)
                selectedPiecePos_y = math.floor(currentMouse_pos[1]//80)
                if 0 <= selectedPiecePos_x < 8 and 0 <= selectedPiecePos_y < 8:
                    if board[selectedPiecePos_y][selectedPiecePos_x].piece is not None:
                        moved_piece = board[selectedPiecePos_y][selectedPiecePos_x].piece
                        selected = True
                        print("Start sqaure: ", selectedPiecePos_x, selectedPiecePos_y)
                else:
                    print("Clicked outside board")
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                destinationMouse_pos = pygame.mouse.get_pos()
                destinationSquare_x = math.floor(destinationMouse_pos[0]//80)
                destinationSquare_y = math.floor(destinationMouse_pos[1]//80)
                if board[destinationSquare_y][destinationSquare_x].piece is not None:
                    #store captured piece
                    captured_piece = board[destinationSquare_y][destinationSquare_x].piece
                    white_captured_pieces.append(captured_piece) if captured_piece.colour == 'w' else black_captured_pieces.append(captured_piece)

                    print("End square: ",destinationSquare_x, destinationSquare_y)
                    print(f"Piece captured: {captured_piece.pieceType} By: {moved_piece.pieceType}")

                else:
                    print("End square: ",destinationSquare_x, destinationSquare_y)    

                #move validations

                if moved_piece.pieceType == 'R':   #rook
                    rook_path_clear = True
                    if destinationSquare_x != selectedPiecePos_x and destinationSquare_y != selectedPiecePos_y:
                        print ("illegal move")
                        rook_path_clear=False
                    else:
                        if destinationSquare_x == selectedPiecePos_x:
                            step = 1 if destinationSquare_y > selectedPiecePos_y else -1
                            for i in range(selectedPiecePos_y + step, destinationSquare_y, step):
                                if board[i][selectedPiecePos_x].piece is not None:
                                    print("Rook path not clear")
                                    rook_path_clear=False
                                    break
                        
                        if destinationSquare_y == selectedPiecePos_y:
                            step = 1 if destinationSquare_x > selectedPiecePos_x else -1
                            for j in range(selectedPiecePos_x + step, destinationSquare_x, step):
                                if board[selectedPiecePos_y][j].piece is not None:
                                    print("Rook path not clear")
                                    rook_path_clear=False
                                    break

                        if rook_path_clear:
                            if board[destinationSquare_y][destinationSquare_x].piece is not None:
                                if moved_piece.colour == board[destinationSquare_y][destinationSquare_x].piece.colour:
                                    print("Rook cannot take own piece")
                                else:
                                    board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                    board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece) 
                            else:
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)   

                        
                if moved_piece.pieceType == 'N':   #knight
                    dx = abs(destinationSquare_x - selectedPiecePos_x)
                    dy = abs(destinationSquare_y - selectedPiecePos_y)

                    if not ((dx == 1 and dy == 2) or (dx == 2 and dy == 1)):
                        print("illegal move for knight")
                        
                    else:
                        if board[destinationSquare_y][destinationSquare_x].piece is not None:
                            if board[destinationSquare_y][destinationSquare_x].piece.colour == moved_piece.colour:
                                print("Knight cannot take own piece")
                            else:
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                        else:
                            board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                            board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                        
                if moved_piece.pieceType == 'B':   #bishop
                    bishop_path_clear = True
                    dx = destinationSquare_x - selectedPiecePos_x
                    dy = destinationSquare_y - selectedPiecePos_y
                    if abs(dx) != abs(dy) or (dx == 0 and dy == 0): # checks allowed scope of moves 
                        print ("Bishop path not clear")
                        bishop_path_clear=False

                    else: # determines available moves
                        step_x = 1 if dx > 0 else -1
                        step_y = 1 if dy > 0 else -1

                        x = selectedPiecePos_x + step_x
                        y = selectedPiecePos_y + step_y

                        while x != destinationSquare_x and y != destinationSquare_y:
                            if board[y][x].piece is not None:
                                print("Bishop path not clear")
                                bishop_path_clear = False
                                break

                            x += step_x
                            y += step_y

                        if bishop_path_clear:
                            if board[destinationSquare_y][destinationSquare_x].piece is not None:
                                if moved_piece.colour == board[destinationSquare_y][destinationSquare_x].piece.colour:
                                    print("Bishop cannot take own piece")
                                else:
                                    board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                    board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece) 
                            else:
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)

                        
                if moved_piece.pieceType == 'Q':   #queen
                    queen_path_clear = True
                    dx = destinationSquare_x - selectedPiecePos_x
                    dy = destinationSquare_y - selectedPiecePos_y

                    if not (destinationSquare_x == selectedPiecePos_x or destinationSquare_y == selectedPiecePos_y or abs(dx) == abs(dy)):
                        print("illegal move for the queen")
                        queen_path_clear = False
                        
                    else:
                        if destinationSquare_x == selectedPiecePos_x or destinationSquare_y == selectedPiecePos_y:
                            if destinationSquare_x == selectedPiecePos_x:
                                step = 1 if destinationSquare_y > selectedPiecePos_y else -1
                                for i in range(selectedPiecePos_y + step, destinationSquare_y, step):
                                    if board[i][selectedPiecePos_x].piece is not None:
                                        print("Queen path not clear")
                                        queen_path_clear = False

                            if destinationSquare_y == selectedPiecePos_y:
                                step = 1 if destinationSquare_x > selectedPiecePos_x else -1
                                for x in range(selectedPiecePos_x + step, destinationSquare_x, step):
                                    if board[selectedPiecePos_y][x].piece is not None:
                                        print("Queen path not clear")
                                        queen_path_clear = False
                            
                            if queen_path_clear:
                                if board[destinationSquare_y][destinationSquare_x].piece is not None:
                                    if moved_piece.colour == board[destinationSquare_y][destinationSquare_x].piece.colour:
                                        print("Queen cannot take own piece")
                                    else:
                                        board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                        board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece) 
                                else:
                                    board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                    board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)

                        if dx==dy:
                            step_x = 1 if dx > 0 else -1
                            step_y = 1 if dy > 0 else -1

                            x = selectedPiecePos_x + step_x
                            y = selectedPiecePos_y + step_y
                            
                            while x != destinationSquare_x and y != destinationSquare_y:
                                if board[y][x].piece is not None:
                                    print("Queen path not clear")
                                    queen_path_clear = False
                                    break

                                x += step_x
                                y += step_y

                            if queen_path_clear:
                                if board[destinationSquare_y][destinationSquare_x].piece is not None:
                                    if moved_piece.colour == board[destinationSquare_y][destinationSquare_x].piece.colour:
                                        print("Queen cannot take own piece")
                                    else:
                                        board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                        board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece) 
                                else:
                                    board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                    board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                        
                if moved_piece.pieceType == 'K':   #king
                    dx = abs(destinationSquare_x - selectedPiecePos_x)
                    dy = abs(destinationSquare_y - selectedPiecePos_y)

                    if not ((dx==1 and dy==0) or (dx==0 and dy==1) or (dx== 1 and dy==1)):
                        print("illegal move for the king")
                        
                    else:
                        if board[destinationSquare_y][destinationSquare_x].piece is not None:
                                if moved_piece.colour == board[destinationSquare_y][destinationSquare_x].piece.colour:
                                    print("King cannot take own piece")
                                else:
                                    board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                    board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece) 
                        else:
                            board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                            board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                
                
                if moved_piece.pieceType == 'P':   # pawn
                    pawn_path_clear = True
                    dx = destinationSquare_x - selectedPiecePos_x
                    dy = destinationSquare_y - selectedPiecePos_y

                    #capturing pieces - with pawns
                    if board[destinationSquare_y][destinationSquare_x].piece is not None:
                        if board[destinationSquare_y][destinationSquare_x].piece.colour != moved_piece.colour:
                            if (abs(dx)==abs(dy)):
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)

                    # determine direction based on color # change when changing sides of the board
                    direction = 1 if moved_piece.colour == 'w' else -1
                    start_rank = 1 if moved_piece.colour == 'w' else 6

                    # straight move
                    if dx == 0:
                        # 1 square move
                        if dy == direction:
                            if board[destinationSquare_y][destinationSquare_x].piece is None:
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                            else:
                                print("illegal move for the pawn")
                        # 2 squares from starting rank
                        elif dy == 2*direction and selectedPiecePos_y == start_rank:
                            intermediate_square_y = selectedPiecePos_y + direction
                            if board[intermediate_square_y][selectedPiecePos_x].piece is None and board[destinationSquare_y][destinationSquare_x].piece is None:
                                board[selectedPiecePos_y][selectedPiecePos_x].remove_pieces()
                                board[destinationSquare_y][destinationSquare_x].receive_pieces(moved_piece)
                            else:
                                print("illegal move for the pawn")
                        else:
                            print("illegal move for the pawn")
                        

                selected = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Entered move:", text)
                last_move.append(text)
                print("moves: ",last_move)
                text = '' # Clear after Enter
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    draw_board()
    side_panel(last_move, colour)
    input_box()

    pygame.display.update()
    clock.tick(60)