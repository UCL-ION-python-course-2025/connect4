import random

import numpy as np

from game_mechanics import (
    choose_move_randomly,
    human_player,
    has_won,
    is_column_full,
    place_piece,
    play_connect_4_game,
)

TEAM_NAME = "Team Name"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"



def choose_move(board): # type: ignore[no-untyped-def]
    """
    This is what will be called during competitive play.
    It takes the current state of the board as input.
    It returns a single move to play.

    Args:
        board: The board as a numpy array. Your pieces are
                1's, the opponent's are -1's and empty are 0's.

    Returns:
        (integer): The column you want to place your counter
                        into (an integer 0 -> 7), where 0 is the
                        far left column and 7 is the far right
                        column.
    """
       # Example solution which chooses a random not-full column to place the counter
    # not_full_columns = []
    # for col in range(8):
    #     if not is_column_full(board, col):
    #         not_full_columns.append(col)
    # return random.choice(not_full_columns)

    raise NotImplementedError("You need to implement this function")



if __name__ == "__main__":


    # Play a game against your bot! Click a column to
    # place a counter!
    play_connect_4_game(
        your_choose_move=human_player,
        opponent_choose_move=choose_move,
        game_speed_multiplier=10,
        render=True,
        verbose=True,
    )
