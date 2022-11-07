from delta_connect4.game_mechanics import load_dictionary, save_dictionary

TEAM_NAME = "test_team"


def test_save_load():

    original_dict = {(1): 1, (2): 2, (3): 3}
    save_dictionary(original_dict, TEAM_NAME)

    load_dict = load_dictionary(TEAM_NAME)

    assert original_dict == load_dict
