## Connect 4 :yellow_circle::red_circle::yellow_circle::red_circle:

Connect 4 is a classic board game.

![Connect 4. Yellow wins with 4 consecutive yellow pieces on a diagonal](images/connect4board.jpeg)

## Rules of Connect 4 :red_circle:

Connect 4 is a **two-player** board game. Players take turns dropping colored counters into a grid. Each player **plays a single color** only. The pieces **fall straight down** to the lowest available space in the column.

**The goal is to form a horizontal, vertical, or diagonal line of 4 of your counters.**

[You can play with your teammate here.](https://boardgames.io/en/connect4)


## The board :yellow_circle: :red_circle:

Unlike typical Connect 4, where there are 7 columns and 6 rows, we’re using **8 columns**. This is to reduce the power of taking the first move. The board is a `6 x 8` `numpy` array.

Numpy arrays are a bit like lists and are used extensively in data analysis in neuroscience.

See `numpy_arrays.md` for an introduction.

For our connect 4 board, the **first axis is the row index** and the **2nd axis is the column index**.

The below image shows this visually. The numbers in square brackets (in the top-left) show how different elements in the array can be referenced.

![Connect 4 board with index of top left squares shown](./images/connect4annotate.png)

The pieces are integers in this array. An empty space is `0`. Your pieces are denoted `1`. Your opponent's pieces are denoted `-1`.

Given a `board` your `choose_move()` function will need to return an integer (between 0 and 7) -  the column to drop your counter in.


## Existing Code :pray:

In the real world (especially if you're analysing data, you will often want to use other people's code for complex stuff you don't want to do yourself. This is good practise for that!)

There are a number of functions already imported into your main.py file. These might help you in your solution 🕵️


```
is_column_full(board, column_idx)

Checks if a board column is full of pieces.
Args:
    board: The board to check
    column_idx: The column to check

Returns:
    True if the column is full, False otherwise
```

```
place_piece(board, column_idx, player)

Place a piece from a player on the board and get the resulting board back.

Args:
    board: board to place the piece on (np array)
    column_idx: column to place the piece in (0 -> 7)
    player: player to place the piece for (1 or -1)

Returns:
    Tuple of (board, row_index) where the board is updated
        and the row_index is the row index of the added piece.
```


```
has_won(board, column_index)

Checks if a player has won based on the most recently-added piece on the board.

Args:
    board: The board to check for a win
    column_index: The column whose top piece you should
                    check for 4-in-a-row

Returns: True if game won, False otherwise
```
