import numpy as np

from delta_connect4.game_mechanics import (
    get_empty_board,
    get_top_piece_row_index,
    has_won,
    is_column_full,
    place_piece,
    reward_function,
)


def test_get_top_piece_row_index():
    board = get_empty_board()

    col = 0
    assert get_top_piece_row_index(board, col) is None

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 5

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 4

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 3

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 2

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 1

    board, _ = place_piece(board, col, 1)
    assert get_top_piece_row_index(board, col) == 0


def test_is_column_full():
    board = get_empty_board()
    assert not is_column_full(board, 0)
    assert not is_column_full(board, 1)
    assert not is_column_full(board, 2)
    assert not is_column_full(board, 3)
    assert not is_column_full(board, 4)
    assert not is_column_full(board, 5)
    assert not is_column_full(board, 6)
    assert not is_column_full(board, 7)

    board, _ = place_piece(board, 0, 1)
    board, _ = place_piece(board, 0, 1)
    board, _ = place_piece(board, 0, 1)
    board, _ = place_piece(board, 0, 1)
    board, _ = place_piece(board, 0, 1)
    board, _ = place_piece(board, 0, 1)
    assert is_column_full(board, 0)
    assert not is_column_full(board, 1)

    board, _ = place_piece(board, 1, 1)
    board, _ = place_piece(board, 1, 1)
    board, _ = place_piece(board, 1, 1)
    board, _ = place_piece(board, 1, 1)
    board, _ = place_piece(board, 1, 1)
    board, _ = place_piece(board, 1, 1)
    assert is_column_full(board, 0)
    assert is_column_full(board, 1)


def test_place_piece():
    board = get_empty_board()

    col = 0
    board, _ = place_piece(board, col, 1)
    assert board[5][0] == 1
    assert np.all(board[0:5, 0] == 0)
    assert np.all(board[6:, 0] == 0)
    assert np.all(board[:, 1:] == 0)
    assert np.sum(board) == 1

    board, _ = place_piece(board, col, 1)
    assert board[4][0] == 1
    assert np.sum(board) == 2
    assert np.all(board[:, 1:] == 0)

    board, _ = place_piece(board, col, 1)
    assert board[3][0] == 1
    assert np.all(board[:, 1:] == 0)
    assert np.sum(board) == 3

    board, _ = place_piece(board, col, 1)
    assert board[2][0] == 1
    assert np.all(board[:, 1:] == 0)
    assert np.sum(board) == 4

    board, _ = place_piece(board, col, 1)
    assert board[1][0] == 1
    assert np.all(board[:, 1:] == 0)
    assert np.sum(board) == 5

    board, _ = place_piece(board, col, 1)
    assert board[0][0] == 1
    assert np.all(board[:, 1:] == 0)
    assert np.sum(board) == 6

    col = 1
    board, _ = place_piece(board, col, 1)
    assert board[5][1] == 1
    assert np.sum(board) == 7
    assert np.all(board[:, 2:] == 0)

    board, _ = place_piece(board, col, 1)
    assert board[4][1] == 1
    assert np.all(board[:, 2:] == 0)
    assert np.sum(board) == 8

    board, _ = place_piece(board, col, 1)
    assert board[3][1] == 1
    assert np.all(board[:, 2:] == 0)
    assert np.sum(board) == 9

    board, _ = place_piece(board, col, 1)
    assert board[2][1] == 1
    assert np.all(board[:, 2:] == 0)
    assert np.sum(board) == 10

    board, _ = place_piece(board, col, 1)
    assert board[1][1] == 1
    assert np.all(board[:, 2:] == 0)
    assert np.sum(board) == 11

    board, _ = place_piece(board, col, 1)
    assert board[0][1] == 1
    assert np.all(board[:, 2:] == 0)
    assert np.sum(board) == 12


def test_has_won():
    board = get_empty_board()

    col = 0
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 1
    player = -1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 1
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 2
    player = -1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 2
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 3
    player = -1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 2
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 3
    player = -1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 3
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 5
    player = -1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == False

    col = 3
    player = 1
    board, _ = place_piece(board, col, player)
    assert has_won(board, col) == True
