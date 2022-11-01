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
    env = Connect4Env()
    env.reset()
    state, reward, done, info = env.step(0)
    assert state is not None
    assert reward == 0
    assert not done
    assert "player_to_take_next_move" in info
    assert state[5][0] == 1
