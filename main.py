import random
from typing import Dict, Tuple

import numpy as np

from check_submission import check_submission
from game_mechanics import (
    Connect4Env,
    choose_move_randomly,
    get_empty_board,
    get_piece_longest_line_length,
    get_top_piece_row_index,
    has_won,
    human_player,
    is_column_full,
    place_piece,
    play_connect_4_game,
)

TEAM_NAME = "Team Steve"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"


def choose_move(state: np.ndarray) -> int:
    return choose_move_randomly(state)


if __name__ == "__main__":

    check_submission(
        TEAM_NAME
    )  # <---- Make sure I pass! Or your solution will not work in the tournament!!

    # Code below plays a single game of Connect 4 against a random
    #  opponent, think about how you might want to adapt this to
    #  test the performance of your algorithm.

    # Play a game against your bot! Click a column to
    # place a counter!
    play_connect_4_game(
        your_choose_move=human_player,
        opponent_choose_move=choose_move,
        game_speed_multiplier=1,
        render=True,
        verbose=True,
    )
