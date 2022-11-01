from pathlib import Path

import delta_utils.check_submission as checker

from game_mechanics import get_empty_board, load_dictionary


def check_submission(team_name: str) -> None:
    example_state = get_empty_board()
    expected_choose_move_return_type = int
    game_mechanics_expected_hash = (
        "2e948aa40139207a623568121ddd8aa7cedd2ba5add39a44f431a9e1daa0b4f9"
    )
    expected_pkl_output_type = dict

    return checker.check_submission(
        example_state=example_state,
        expected_choose_move_return_type=expected_choose_move_return_type,
        expected_pkl_type=expected_pkl_output_type,
        pkl_file=load_dictionary(team_name),
        pkl_checker_function=checker.pkl_checker_value_dict,
        game_mechanics_hash=game_mechanics_expected_hash,
        current_folder=Path(__file__).parent.resolve(),
    )
