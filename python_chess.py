"""CLI CHESS GAME"""   #GUI

import chess, os, requests, random

board=chess.Board()

def clear_terminal(depth):
    #clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Enter 'stop' to end game")
    if depth == "0":
        print(f"Engine Depth - [5]")
    else:
        print(f"Engine depth [{depth}]")


# register and print moves
listOfMoves=[]
def logging_moves(turn, move):
    #records move based on whos turn it is.
    if turn:
        listOfMoves.append(move)
    else:
        listOfMoves[-1] = f"{listOfMoves[-1]}, {move}"


    #print as a numbered list
    recent_moves = listOfMoves[-3:]
    for i, move_made in enumerate(recent_moves, start=max(0, len(listOfMoves) - 3)+1):
        print(f"{i}. {move_made}")


def push_player_move(player_move):
    board.push_san(player_move)

# STOCKFISH MOVES
def push_bot_move(depth):
    """get move from stockfish, clear terminal, record move"""

    if depth is None:
        depth=5
    try:
        url = "https://stockfish.online/api/s/v2.php"
        parameters = {"fen": board.fen(), "depth": depth}
        response = requests.get(url, params=parameters, timeout=5)
        move_dict = response.json()
        best_move = move_dict["bestmove"].split() #access best move and convert to move object, splits at whitespaces by default hence no argument
        bot_move = board.san(chess.Move.from_uci(best_move[1])) #one-liner converting from uci to san to record in history
        board.push_san(bot_move)

        return bot_move

    except (requests.exceptions.RequestException, KeyError, ValueError):
        #if API fails

        #random move
        #legal_moves = list(board.legal_moves)
        #bot_move = board.san(random.choice(legal_moves))
        #board.push_san(bot_move)

        #terminate game
        return "terminated"


def gameplay(player_colour, depth):
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
            turn = board.turn
            if player_colour == board.turn:
                player_move = input("Enter Move(SAN): ")
                if player_move.lower().strip() == "stop":
                    print("GameTerminated")
                    break
                try:
                    push_player_move(player_move)
                    move=player_move
                    clear_terminal(depth)
                    if not player_colour:
                        flipped_board = str(board)[::-1]
                        print(flipped_board)
                    else:
                        print(board)
                    logging_moves(turn=turn, move=move)
                except (ValueError, chess.IllegalMoveError, chess.AmbiguousMoveError):
                    print("Invalid Move")
            else:
                move=push_bot_move(depth)
                if move == "terminated":
                    print("API Failure - GameTerminated")
                    return
                
                clear_terminal(depth)
                if not player_colour:
                    flipped_board = str(board)[::-1]
                    print(flipped_board)
                else:
                    print(board)
                logging_moves(turn=turn, move=move)

#Body of program
def main():
    print("CLI Chess Game")
    print("Moves must be in Standard Algebraic Notation")
    print("Enter 'stop' to end game")
    print(board)

    while True:
        #setting engine depth
        depth = input("Engine Depth: ")
        try:
            if depth == "stop":
                print("GameTerminated")
                return
            elif depth =="0":
                depth = None
                break
            elif (4<int(depth.strip())<16):
                depth = int(depth)
                break
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")

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
            print("Spelling or Invalid input")

    gameplay(player_colour=player_colour, depth=depth)

if __name__ == '__main__':
    main()