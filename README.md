# game-template

## Template usage

Press the 'use this template button' and enter the name of the game.

Clone the game

Install the pre-commit and pre-push hooks

```bash
pre-commit install --hook-type pre-commit --hook-type pre-push
```

## Install a game locally

Edit `setup.py` with the name of the game etc

Then run (in this folder)

```bash
pip install -e .
```

the -e flag makes the game editable. So you can make changes with pip installing afterwards

Usage

```python
from gamename import game_mechanics
```


## Instantiate a game on replit

Follow [these](https://www.notion.so/How-to-init-a-Replit-from-GitHub-877ee57054444a0085e884401e80d02b) instructions

You should only see `main.py` and `game_mechanics.py`. All other files should be hidden by `.replit`

## To push to github from a replit

```
git -c "user.name=YOURUSENAME" -c "user.email=YOUREMAIL" commit -m "COMMIT MESSAGE"
```

(add a PAT when prompted for password)


