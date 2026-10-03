"""CLI CHESS GAME"""   #BRANCH DUPLICATION | CHOOSE ENGINE DEPTH | PRINT ONLY MOST RECENT MOVE

import chess, os, requests, random

def clear_terminal():
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("CLI chess game")
    print("Enter 'stop' to end game")
    print("Moves must be in SAN")

    return

# register and print moves
def loggingMoves(player_colour, botMove=None, player_move=None):
    #logs the move of whoever played first.
    # when the second person plays, it pops it from the list to add both as one line
    if player_colour:
        if botMove==None:
            listOfMoves.append(player_move)
        else:
            listOfMoves.pop()
            listOfMoves.append(player_move+", "+botMove)
    else:
        if player_move == None:
            listOfMoves.append(botMove)
        else:
            listOfMoves.pop()
            listOfMoves.append(str(botMove)+", "+player_move)

    for i, move in enumerate(listOfMoves, start=1): #prints as a numbered list
        print(f"{i}. {move}")

    return

def push_player_move(player_move):
    board.push_san(player_move)
    return

# STOCKFISH MOVES
def push_bot_move():
    """get move from stockfish, clear terminal, record move"""
    try:
        url = "https://stockfish.online/api/s/v2.php"
        parameters = {"fen": board.fen(), "depth": 5}
        response = requests.get(url, params=parameters, timeout=5)
        move_dict = response.json()
        best_move = move_dict["bestmove"].split() #access best move and convert to move object, splits at whitespaces by default hence no argument
        bot_move = board.san(chess.Move.from_uci(best_move[1])) #one liner converting from uci to san to record in history
        board.push_san(bot_move)
    
    except (requests.exceptions.RequestException, KeyError, ValueError):

        #random move generator if API fails
        legalMoves = list(board.legal_moves)
        bot_move = board.san(random.choice(legalMoves))
        board.push_san(bot_move)
    
    return bot_move

board = chess.Board()
listOfMoves=[]

#Body of program
def main():
    print("CLI chess game")
    print("Enter 'stop' to end game!")
    print("Moves must be in SAN")
    while True:
        option=input("Black or White?: ")

        #setting player_colour as bool for easier handling
        if option.lower().strip() == "white":
            player_colour = True
            break
        elif option.lower().strip() == "black":
            player_colour=False
            break
        elif option.lower().strip() == "stop":
            print("Game Terminated")
            return
        else:
            print("Spelling or Invalid option")

    #if user selects black
    if not player_colour:
        while True:
            if board.is_game_over(claim_draw=True): #check if game is over
                print(f"GameOver")
                outcome = board.outcome(claim_draw=True)
                if outcome.termination.name != 'CHECKMATE':
                    print("The game is a draw")
                    break
                else:
                    winner = 'White' if outcome.winner else 'Black'
                    print(f"{winner} won by {outcome.termination.name}")
                    break
            else:   
                if board.turn: #check whos turn it is
                    botMove=push_bot_move()
                    clear_terminal()
                    print(str(board)[::-1]) #flip board
                    loggingMoves(player_colour=player_colour, botMove=botMove)
                else:
                    player_move = input("Enter move: ")
                    if player_move.lower().strip()=='stop':
                        print("GameTerminated")
                        break

                    try:
                        push_player_move(player_move)
                        clear_terminal()
                        print(str(board)[::-1])
                        loggingMoves(player_colour, player_move=player_move, botMove=botMove)

                    except (ValueError, chess.IllegalMoveError, chess.AmbiguousMoveError):
                        print("Invalid Move")            

    else: #if user selects white
        print(board)
        while True:
            if board.is_game_over(claim_draw=True): #check if game is over
                print(f"GameOver")
                outcome = board.outcome(claim_draw=True)
                if outcome.termination.name != 'CHECKMATE':
                    print("The game is a draw")
                    break
                else:
                    winner = 'White' if outcome.winner else 'Black'
                    print(f"{winner} won by {outcome.termination.name}")
                    break
            else:   
                if board.turn: #check whos turn it is
                    player_move = input("Enter move: ")
                    if player_move.lower().strip()=='stop':
                        print("GameTerminated")
                        break
                    try:
                        push_player_move(player_move)
                        clear_terminal()
                        print(board)
                        loggingMoves(player_colour, player_move=player_move)

                    except (ValueError, chess.IllegalMoveError, chess.AmbiguousMoveError):
                        print("Invalid move")

                else:
                    botMove=push_bot_move()
                    clear_terminal()
                    print(board)
                    loggingMoves(player_colour, botMove, player_move)
    
    return

if __name__ == '__main__':
    main()