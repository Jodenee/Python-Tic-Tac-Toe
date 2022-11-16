from gameClasses import *

player1: Player = Player("player1", "X")
player2: Player = Player("player2", "O")
gameInstance: Game = Game(player1=player1, player2=player2)

def display_win_message() -> None:
    gameInstance.grid.render_grid()
    print(f"Winner: {gameInstance.winner.id}\nTime Elapsed: {round(gameInstance.end_time - gameInstance.start_time, 2)}s")   

def display_tie_message() -> None:
    gameInstance.grid.render_grid()
    print(f"It's a tie.\nTime Elapsed: {round(gameInstance.end_time - gameInstance.start_time, 2)}s")

while True:
    gameInstance.grid.render_grid()

    while True:
        try:
            play = gameInstance.grid.get_gridbox(int(input(f"{gameInstance.current_turn.id} Make a play: ")))
        except IndexError:
            print("\nNo such gridbox exists. Try again.\n")
            continue
        except ValueError:
            print("\nPlease Input a valid number.\n")
            continue
        except KeyError:
            print("\nNo such gridbox exists. Try again.\n")
            continue
        else:
            if gameInstance.can_player_play(play): 
                gameInstance.play(gameInstance.current_turn, play)
            else:
                print("\nThat gridbox is already taken.\n")
                continue

        break
    
    if gameInstance.check_for_win(gameInstance.current_turn): 
        display_win_message()
        break
    if gameInstance.check_for_tie(): 
        display_tie_message()
        break

    if gameInstance.current_turn == player1:
        gameInstance.current_turn = player2
    else:
        gameInstance.current_turn = player1

input("\nPress Enter to end process. . .\n")