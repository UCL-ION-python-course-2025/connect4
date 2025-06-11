import numpy as np

from delta_connect4.game_mechanics import Connect4Env


def test_init():
    env = Connect4Env()
    assert env is not None


def test_reset():
    env = Connect4Env()
    state, reward, done, info = env.reset()
    assert state is not None
    assert reward == 0
    assert not done
    assert "player_to_take_next_move" in info


def test_step():

    # From get_empty_board()
    num_rows: int = 6
    num_cols: int = 8

    env = Connect4Env()
    env.reset()
    state, reward, done, info = env.reset()
    assert reward == 0
    assert state is not None
    assert not done

    reset_took_move = False
    if np.sum(state == 0) != num_rows * num_cols:
        assert np.sum(state != 0) == 1
        assert np.sum(state == -1) == 1
        reset_took_move = True

    assert info["player_to_take_next_move"] == 1

    state, reward, done, info = env.step(0)
    assert state is not None
    assert reward == 0
    assert not done
    assert "player_to_take_next_move" in info
    if reset_took_move:
        assert np.sum(state != 0) == 3
        assert np.sum(state == -1) == 2
        assert np.sum(state == 1) == 1
    else:
        assert state[5][0] == 1
        assert np.sum(state != 0) == 2
        assert np.sum(state == -1) == 1
        assert np.sum(state == 1) == 1


def test_step_50_times():
    for _ in range(50):
        test_step()
