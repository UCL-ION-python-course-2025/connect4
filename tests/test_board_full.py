import itertools

from delta_connect4.game_mechanics import board_full, get_empty_board, place_piece


def test_board_full():
    board = get_empty_board()
    assert not board_full(board)

    n_rows = 6
    n_cols = 8

    for n, (col, _) in enumerate(itertools.product(range(n_cols), range(n_rows))):
        piece = n % 2 * 2 - 1
        board, _ = place_piece(board, col, piece)

        if n < n_cols * n_rows - 1:
            assert not board_full(board)
        else:
            assert board_full(board)

    assert board_full(board)
