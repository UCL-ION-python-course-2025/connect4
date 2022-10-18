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
    is_column_full,
    load_dictionary,
    place_piece,
    play_connect_4_game,
    reward_function,
    save_dictionary,
    human_player,
)


TEAM_NAME = "Team Name"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", "Please change your TEAM_NAME!"


def to_feature_vector(state: np.ndarray) -> Tuple:
    """
    TODO: Write this function to convert the state to a
           feature vector.

    We suggest you use functions in game_mechanics.py to
     make a handcrafted feature vector based on the
     state of the board.

    Args:
        state: board state as a np array. 1's are your
               pieces. -1's your opponent's pieces & 0's
               are empty.

    Returns:
        the feature vector for this state, as
         designed by you.
    """
    raise NotImplementedError("You need to implement the to_feature_vector() function! :)")


def train() -> Dict:
    """
    TODO: Write this function to train your algorithm.

    Returns:
        Value function dictionary used by your agent.
         You can structure this how you like, but
         choose_move() expects {feature_vector: value}.
    """
    raise NotImplementedError("You need to implement the train() function!")


def choose_move(state: np.ndarray, value_function: Dict, verbose: bool = False) -> int:
    """
    Called during competitive play. It acts greedily given
    current state of the board and value function dictionary.
    It returns a single move to play.

    Args:
        state: State of the board as a np array. Your pieces are
                1's, the opponent's are -1's and empty are 0's.
        value_function: The dictionary output by train().

    Returns:
        position (int): The column you want to place your counter
                        into (an integer 0 -> 7), where 0 is the
                        far left column and 7 is the far right
                        column.
    """
    values = []
    not_full_cols = [col for col in range(state.shape[1]) if not is_column_full(state, col)]

    for not_full_col in not_full_cols:
        # Do 1-step lookahead and compare values of successor states
        state_copy = state.copy()
        place_piece(board=state_copy, column_idx=not_full_col, player=1)

        # Get the feature vector associated with the successor state
        features = to_feature_vector(state_copy)
        if verbose:
            print(
                "Column index:",
                not_full_col,
                "Feature vector:",
                features,
                "Value:",
                value_function.get(features, 0),
            )

        # Add the action value to the values list
        action_value = value_function.get(features, 0) + reward_function(not_full_col, state_copy)
        values.append(action_value)

    # Pick randomly between max value actions
    max_value = max(values)
    value_indices = [index for index, value in enumerate(values) if value == max_value]
    value_index = random.choice(value_indices)
    return not_full_cols[value_index]


if __name__ == "__main__":
    # Example workflow, feel free to edit this! ###
    my_value_fn = train()
    save_dictionary(my_value_fn, TEAM_NAME)

    check_submission(
        TEAM_NAME
    )  # <---- Make sure I pass! Or your solution will not work in the tournament!!

    my_value_fn = load_dictionary(TEAM_NAME)

    # Code below plays a single game of Connect 4 against a random
    #  opponent, think about how you might want to adapt this to
    #  test the performance of your algorithm.
    def choose_move_no_value_fn(state: np.ndarray) -> int:
        """
        The arguments to play_connect_4_game() require functions that
            only take the state as input.
        """
        return choose_move(state, my_value_fn)

    # Play a game against your bot! Click a column to
    # place a counter!
    play_connect_4_game(
        your_choose_move=human_player,
        opponent_choose_move=choose_move_no_value_fn,
        game_speed_multiplier=10,
        render=True,
        verbose=True,
    )
