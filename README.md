## RL to play Connect 4 :yellow_circle::red_circle::yellow_circle::red_circle:

Connect 4 is a classic board game.

![Connect 4. Yellow wins with 4 consecutive yellow pieces on a diagonal](images/connect4board.jpeg)

## Rules of Connect 4 :red_circle:

Connect 4 is a **two-player** board game. Players take turns dropping colored counters into a grid. Each player **plays a single color** only. The pieces **fall straight down** to the lowest available space in the column.

**The goal is to form a horizontal, vertical, or diagonal line of 4 of your counters.**

[You can play with your teammate here.](https://boardgames.io/en/connect4)

Your task is to build a **Reinforcement Learning agent** that plays **Connect 4**

# Competition Rules :crossed_swords:

## 1. You must build a **Reinforcement Learning** agent.
- Rules-based agents **aren't allowed**!
## 2. You can only write code in `main.py`
- You can only store data in a dictionary (saved in a `.pkl` file by `save_dictionary()`*)
- In the competition, your agent will call the `choose_move()` function in `main.py` to select a move
- Any code not in `main.py` **will not be used**.
- **Check your submission is valid with `check_submission()`**

*`save_dictionary()` is a function in `game_mechanics.py`

## 3. Submission deadline: **5pm UTC, Sunday**.
- You can update your code after submitting, but **not after the deadline**.
- Check your submission is valid with `check_submission()`

## Competition Format :crossed_swords:

The competition will consist of your AI playing other teams' AIs 1-v-1 in a knockout tournament.

Every 1-v-1 matchup consists of 2 games with the **first player to play** chosen randomly in the first game. The 2nd game is started by the other player. If one team hasn't won more games than the other, there are two possible game outcomes:

1. Draw-Draw: the two players are judged to be equivalent and both progress as one team.
2. Win-Lose: the player whose win took fewer moves wins the overall tie. If they took the same number of moves in both wins, it's equivalent to Draw-Draw

The competition & discussion will be in [Gather Town](https://app.gather.town/app/nJwquzJjD4TLKcTy/Delta%20Academy) at **6pm UTC on Sunday** (1 hour after submission deadline)!

![Example knockout tournament tree](./images/tournament_tree.png)

## Technical Details :hammer:

We strongly suggest you use a feature lookup table. Read `feature_vectors.md` for a short recap of feature vectors.

### States :yellow_circle:

Unlike typical Connect 4, where there are 7 columns and 6 rows, we’re using **8 columns**. This is to reduce the power of taking the first move. The board is a `6 x 8` `numpy` array.

The **first axis is the row index** and the **2nd axis is the column index**.

The below image shows this visually. The numbers in square brackets (in the top-left) show how different elements in the array can be referenced.

![Connect 4 board with index of top left squares shown](./images/connect4annotate.png)

The pieces are integers in this array. An empty space is `0`. Your pieces are denoted `1`. Your opponent's pieces are denoted `-1`.

Since there are `3 ** 48 = 1e23` possible states, we strongly suggest you use feature vectors to reduce the state space. See `feature_vectors.md` in this repl for more a refresher on feature vectors.

### Actions :axe:

**The actions correspond to the index (`0` -> `7`) of the column to drop your counter into.**

In the above diagram, this is the number on the **2nd Axis**. The index of a column that is full (there are no spaces left) is an invalid action.

### Rewards :moneybag:

| Step | Reward |
|------|------|
|  You win | `+1` |
|  You lose | `-1` |
|  All other steps | `0` |


## Functions you write :point_left:

<details>
<summary><code style="white-space:nowrap;">  to_feature_vector()</code></summary>
Write this to convert a state into a feature vector. These features are used to represent the state in the value function lookup table.
<br />

<br />
Input is the state (<code style="white-space:nowrap;">np.array</code>) and output is a <code style="white-space:nowrap;">tuple</code> which you design! The better the features you pick out, the faster your agent will learn and better it can be at Connect-4.
<br />

<br />
Too detailed of a feature vector and it'll take a long time to train. Not enough detail and your agent will hit a ceiling since too many varied states will look identical.
<br />
<br />
E.g. if your feature was just "number of pieces played by me", there are many different states with the same number of pieces played (and thus the same value function).
</details>

<details>
<summary><code style="white-space:nowrap;">  train()</code></summary>
Write this to train your value function dictionary from experience in the environment. Use TD learning.
<br />
<br />
Output the trained dictionary so it can be saved.
<br />
<br />
You can structure your value dictionary however you like,
but the existing implementation of <code style="white-space:nowrap;">choose_move()</code> expects <code style="white-space:nowrap;">{feature_vector: value}</code>.
<br />
<br />
If you structure it another way, you'll have to tweak <code style="white-space:nowrap;">choose_move()</code>
</details>

## Existing Code :pray:

### Need to Know

<details>
<summary><code style="white-space:nowrap;">  Connect4Env</code> class</summary>
The environment class controls the game and runs the opponent's <code style="white-space:nowrap;">choose_move()</code> function.
<br />
<br />
Use it to train your agent. See example usage in <code style="white-space:nowrap;">play_connect_4_game()</code>.
<br />
<br />
The opponent's <code style="white-space:nowrap;">choose_move()</code> function is input at initialisation (when <code style="white-space:nowrap;">Connect4Env(opponent_choose_move)</code> is called).
<br />
<br />
The first player is chosen at random when <code style="white-space:nowrap;">Connect4Env.reset()</code> is called. Every time you call <code style="white-space:nowrap;">Connect4Env.step()</code>, 2 moves are taken - yours and then your opponent's. Your opponent sees a 'flipped' version of the board, where their pieces are shown as <code style="white-space:nowrap;">1</code>'s and yours are shown as <code style="white-space:nowrap;">-1</code>'s.
    <br />
    <br />
Connect4Env takes 3 optional arguments:

- <code style="white-space:nowrap;">verbose</code> Whether to print the board and logging information (such as the position of the move recent move) to the console.
- <code style="white-space:nowrap;">render</code> Whether to render the game graphically. The player plays with red counters and the opponent players with yellow. Set this to True if you want to play against your bot yourself.
- <code style="white-space:nowrap;">game_speed_multiplier</code> How fast to render a game (only has an effect when render= True). Low number = slow. High number = fast.

</details>

<details>
<summary><code style="white-space:nowrap;">  choose_move()</code></summary>
This acts greedily given the <code style="white-space:nowrap;">state</code> and value function dictionary. We've given you this to save time, but you are welcome to change it.
<br />
<br />
In the competition, <code style="white-space:nowrap;">choose_move()</code> selects your moves. Takes the state as input and outputs an action.
<br />
<br/>
This takes an optional <code style="white-space:nowrap;">verbose</code> argument, which outputs information useful for debugging when set toe <code style="white-space:nowrap;">True</code>.
</details>

<details>
<summary><code style="white-space:nowrap;">  human_player()</code></summary>
Input into <code style="white-space:nowrap;">play_connect_4_game()</code> to play yourself.
<br />
<br />
Click on the column to play a counter there.
</details>

<details>
<summary><code style="white-space:nowrap;">  choose_move_randomly()</code></summary>
Like above, but randomly picks from non-full columns.
<br />
<br />
Takes the state as input and outputs an action.
</details>


<details>
<summary><code style="white-space:nowrap;">  reward_function()</code></summary>
What reward would be received in state 'successor_state' after taking action 'last_action_taken'
<br />
<br />
Takes the state and an action as input and outputs a float
</details>

<details>
<summary><code style="white-space:nowrap;">  place_piece()</code></summary>
The transition function. Returns a tuple of ('board', 'row'), where 'board' is the 'board' after a piece has been placed in 'column_idx' by 'player'.
<br />
</details>


<details>
<summary><code style="white-space:nowrap;">  play_connect_4_game()</code></summary>
Plays 1 game of Connect 4, which can be visualsed either in the console (if <code style="white-space:nowrap;">verbose=True</code>) or rendered visually (if <code style="white-space:nowrap;">render = True</code>). Outputs the return for your agent.
<br />
<br />
Inputs:

<code style="white-space:nowrap;">your_choose_move</code>: Function that takes the state and outputs the action for your agent.

<code style="white-space:nowrap;">opponent_choose_move</code>: Function that takes the state and outputs the action for the opponent.

<code style="white-space:nowrap;">game_speed_multiplier</code>: controls the gameplay speed. High numbers mean fast games, low numbers mean slow games.

<code style="white-space:nowrap;">render</code>: whether to render the game visually.

<code style="white-space:nowrap;">verbose</code>: whether to print to console each move and the corresponding board states.

</details>

## Other code :gear:

There are **a load** of functions in `game_mechanics.py`. The useful functions are clearly indicated and are explained in their docstrings.

We suggest you use these to form your features. However, **you cannot change the `game_mechanics.py` file**. The original will be used in the competition.

If you want to tweak one of these functions, copy-paste it to `main.py` and rename it.

## Suggested Approach :+1:

1. Discuss which features should be in the feature vector - what corresponds with a good Connect 4 game state? What about a bad one?
2. **Write `train()`**, borrowing from past exercises
3. **Iterate, iterate, iterate** on that `to_feature_vector()` function
