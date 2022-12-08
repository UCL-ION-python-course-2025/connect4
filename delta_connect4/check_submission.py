from pathlib import Path

from delta_utils import get_discrete_choose_move_out_checker, pkl_checker_value_dict
from delta_utils.check_submission import check_submission as _check_submission
from game_mechanics import get_empty_board, load_dictionary


def check_submission(team_name: str) -> None:
    pkl_checker_value_dict(load_dictionary, team_name, dict)
    pkl_file = load_dictionary(team_name)
    return _check_submission(
        example_choose_move_input={
            "state": get_empty_board(),
            "value_function": pkl_file,
            "verbose": False,
        },
        check_choose_move_output=get_discrete_choose_move_out_checker(
            possible_outputs=list(range(8))
        ),
        current_folder=Path(__file__).parent.resolve(),
    )
