from delta_connect4.game_mechanics import get_empty_board, has_won, place_piece, reward_function


def test_reward_function_single_player():
    board = get_empty_board()

    col = 0
    board, _ = place_piece(board, col, 1)
    assert reward_function(col, board) == 0

    board, _ = place_piece(board, col, 1)
    assert reward_function(col, board) == 0

    board, _ = place_piece(board, col, 1)
    assert reward_function(col, board) == 0

    board, _ = place_piece(board, col, 1)
    assert reward_function(col, board) == 1


def test_reward_function_mutliplayer():
    board = get_empty_board()

    col = 0
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 0
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 0
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 0
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 0
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 0
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 1
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 1
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 2
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 2
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 3
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 1


def test_reward_function_diagonal():
    board = get_empty_board()

    col = 0
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 1
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 1
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 2
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 2
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 3
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 2
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 3
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 3
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 5
    player = -1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 0

    col = 3
    player = 1
    board, _ = place_piece(board, col, player)
    assert reward_function(col, board) == 1
